import google.generativeai as genai
from app.utils.config import GEMINI_API_KEY
import json

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

def extract_skills_from_resume(resume_text: str):
    if not GEMINI_API_KEY:
        return {
            "error": "GEMINI_API_KEY is missing.",
            "technical_skills": ["General Tech"],
            "soft_skills": ["Communication"]
        }

    model = genai.GenerativeModel("models/gemini-2.0-flash")
    
    prompt = f"""
    Extract technical and professional skills from the following resume text.

    Return output strictly in this JSON format:
    {{
        "technical_skills": [],
        "soft_skills": []
    }}

    Resume:
    {resume_text}
    """

    try:
        response = model.generate_content(prompt)
        # Clean the response in case Gemini adds markdown backticks
        text_response = response.text.replace("```json", "").replace("```", "").strip()
        try:
            return json.loads(text_response)
        except:
            return {
                "technical_skills": [],
                "soft_skills": []
            }
            
    except Exception as e:
        # Fallback to Demo Data if Rate Limited (429) or other error
        print(f"Gemini API Error: {str(e)}")
        
        # Simple keyword matching for demo purposes
        keywords = ["python", "javascript", "react", "html", "css", "sql", "design", "figma", "ui", "ux", "fastapi"]
        found = [k for k in keywords if k in resume_text.lower()]
        
        demo_response = {
            "is_demo_mode": True,
            "api_error": f"AI Error: {str(e)}. Showing demo results.",
            "technical_skills": found if found else ["General Tech"],
            "soft_skills": ["Communication", "Teamwork", "Problem Solving"]
        }
        return demo_response
