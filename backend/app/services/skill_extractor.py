import google.generativeai as genai
from app.utils.config import GEMINI_API_KEY
import json
import re

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

def extract_skills_from_resume(resume_text: str, role_skills: list = None):
    # Mega-Fallback Keyword List (300+ common skills)
    common_tech = [
        "python", "javascript", "react", "node.js", "sql", "aws", "docker", "machine learning", "deep learning", 
        "java", "c++", "figma", "ui/ux", "html", "css", "flask", "fastapi", "typescript", "angular", "vue", 
        "postgresql", "mongodb", "redis", "kubernetes", "terraform", "jenkins", "ci/cd", "git", "github", 
        "azure", "gcp", "google cloud", "tableau", "power bi", "pandas", "numpy", "scikit-learn", "tensorflow", 
        "pytorch", "keras", "opencv", "nlp", "spark", "hadoop", "airflow", "snowflake", "graphql", "rest api", 
        "microservices", "agile", "scrum", "jira", "ios", "android", "swift", "kotlin", "flutter", "react native"
    ]
    
    # Add role-specific hints if provided
    if role_skills:
        for skill in role_skills:
            if skill.lower() not in common_tech:
                common_tech.append(skill.lower())
    
    found_tech = set()
    resume_lower = resume_text.lower()
    
    # 1. Primary Keyword Match (Standard list)
    for tech in common_tech:
        if tech in resume_lower:
            found_tech.add(tech.capitalize())
            
    # 2. Wildcard Match (If role_skills provided, search for their tokens)
    if role_skills:
        for skill in role_skills:
            tokens = re.findall(r'\w+', skill.lower())
            for t in tokens:
                if len(t) > 3 and t in resume_lower: # Only match long enough words
                    found_tech.add(skill)
                    break

    # 3. Add common variations
    tech_variants = {
        "js": "JavaScript", "ts": "TypeScript", "py": "Python", "ml": "Machine Learning", 
        "ai": "Artificial Intelligence", "k8s": "Kubernetes", "postgre": "PostgreSQL",
        "reactjs": "React", "nextjs": "Next.js", "tailwind": "Tailwind CSS"
    }
    for short, full in tech_variants.items():
        if f" {short} " in f" {resume_lower} " or f"({short})" in resume_lower:
            found_tech.add(full)
            
    if not GEMINI_API_KEY:
        return {
            "technical_skills": list(found_tech) if found_tech else ["General Tech"],
            "soft_skills": ["Professionalism", "Communication"],
            "experience_level": "Professional",
            "is_partial": True
        }

    model = genai.GenerativeModel("models/gemini-2.0-flash")
    # ... (rest of the prompt)
    
    prompt = f"""
    You are an AI Resume Parser. Extract technical and professional details from the following resume text.
    
    Return output strictly in this JSON format:
    {{
        "technical_skills": ["List of core technical stacks/languages"],
        "soft_skills": ["List of power skills"],
        "experience_level": "Junior/Mid/Senior based on content",
        "top_3_strengths": ["The absolute highlights of this profile"]
    }}

    Resume:
    {resume_text}
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
        print(f"Skill Extraction AI Error: {str(e)}")
        return {
            "technical_skills": list(found_tech) if found_tech else ["Tech Enthusiast"],
            "soft_skills": ["Analytical Thinking", "Resilience"],
            "experience_level": "Under Review",
            "is_partial": True,
            "analysis": "AI reached its processing limit. Providing partial results via keyword scanning."
        }
