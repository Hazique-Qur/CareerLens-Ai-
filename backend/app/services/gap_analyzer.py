import google.generativeai as genai
from app.utils.config import GEMINI_API_KEY
import json
import re

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

def analyze_skill_gap(user_skills: list, required_skills: list):
    # Base fallback logic (shared between API-missing and API-failure)
    user_skills_lower = [s.lower() for s in user_skills]
    matched_base = []
    for req in required_skills:
        req_l = req.lower()
        if any(req_l in us or us in req_l for us in user_skills_lower):
            matched_base.append(req)
    
    missing_base = [s for s in required_skills if s not in matched_base]
    
    if not GEMINI_API_KEY:
        score = (len(matched_base) / len(required_skills) * 100) if required_skills else 5
        return {
            "match_score": round(score, 2), 
            "matched_skills": matched_base, 
            "missing_skills": missing_base,
            "is_partial": True,
            "analysis": "Manual matching active. AI currently unavailable."
        }

    model = genai.GenerativeModel("models/gemini-2.0-flash")
    
    prompt = f"""
    You are a Senior Technical Recruiter. Compare the User's Skills against the Required Skills for a role.
    Use semantic matching (e.g., "GCP" matches "Google Cloud", "Vue.js" matches "Vue").
    
    User Skills: {user_skills}
    Required Skills: {required_skills}

    Return a JSON object with:
    1. "match_score": (0-100) based on importance and coverage.
    2. "matched_skills": list of required skills that the user possesses (semantically).
    3. "missing_skills": list of required skills the user lacks.
    4. "analysis": A brief 1-sentence expert summary of the gap.

    Format: {{"match_score": 85, "matched_skills": [], "missing_skills": [], "analysis": ""}}
    """

    try:
        response = model.generate_content(prompt)
        text = response.text.strip()
        
        # Robust JSON extraction
        json_match = re.search(r'\{.*\}', text, re.DOTALL)
        if json_match:
            text = json_match.group(0)
            
        result = json.loads(text)
        result["is_partial"] = False
        return result
    except Exception as e:
        print(f"Gap Analysis AI Error: {str(e)}")
        # Honest fallback: dynamic score based on substring matching
        matches = len(matched_base)
        reqs = len(required_skills)
        score = (matches / reqs * 100) if reqs else 5
        # Add a tiny "bonus" if there are any matches at all, to avoid 0% for partial hits
        if matches > 0: score = max(score, 10.0)
        
        return {
            "match_score": round(score, 2), 
            "matched_skills": matched_base, 
            "missing_skills": missing_base,
            "is_partial": True,
            "analysis": "AI reached its processing limit. Providing partial analysis results based on direct skill matches."
        }
