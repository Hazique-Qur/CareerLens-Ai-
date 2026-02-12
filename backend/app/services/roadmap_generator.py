import google.generativeai as genai
from app.utils.config import GEMINI_API_KEY
import json

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

def generate_roadmap(target_role: str, missing_skills: list):
    if not GEMINI_API_KEY:
        return {
            "error": "GEMINI_API_KEY is missing.",
            "learning_roadmap": [],
            "project_suggestions": [],
            "interview_questions": []
        }

    model = genai.GenerativeModel("models/gemini-1.5-pro-latest")
    
    prompt = f"""
    A candidate wants to become a {target_role}.
    They are missing these skills: {missing_skills}

    Generate:

    1. A 3-step learning roadmap (each step with 'topic', 'description', 'difficulty', and 'resource_url')
    2. Recommended project ideas (short strings)
    3. 5 interview questions based on missing skills

    Return strictly in JSON format:

    {{
        "learning_roadmap": [
            {{ "topic": "...", "description": "...", "difficulty": "Beginner/Intermediate/Advanced", "resource_url": "..." }},
            {{ "topic": "...", "description": "...", "difficulty": "Beginner/Intermediate/Advanced", "resource_url": "..." }},
            {{ "topic": "...", "description": "...", "difficulty": "Beginner/Intermediate/Advanced", "resource_url": "..." }}
        ],
        "project_suggestions": ["string", "string"],
        "interview_questions": ["string", "string", "string", "string", "string"]
    }}
    """

    try:
        response = model.generate_content(prompt)
        text_response = response.text.replace("```json", "").replace("```", "").strip()
        
        try:
            return json.loads(text_response)
        except:
            return {
                "learning_roadmap": [],
                "project_suggestions": [],
                "interview_questions": []
            }
            
    except Exception as e:
        print(f"Roadmap Gemini Error: {str(e)}")
        # Enhanced Fallback Data
        return {
            "learning_roadmap": [
                {
                    "topic": "Advanced Data Structures", 
                    "description": "Master trees, graphs, and dynamic programming for optimized solutions.", 
                    "difficulty": "Advanced", 
                    "resource_url": "https://neetcode.io/"
                },
                {
                    "topic": "System Design Patterns", 
                    "description": "Learn how to scale applications using microservices and load balancing.", 
                    "difficulty": "Intermediate", 
                    "resource_url": "https://github.com/donnemartin/system-design-primer"
                },
                {
                    "topic": "Cloud Infrastructure (AWS/Azure)", 
                    "description": "Deploy and manage containerized applications in the cloud.", 
                    "difficulty": "Intermediate", 
                    "resource_url": "https://aws.amazon.com/training/"
                }
            ],
            "project_suggestions": [
                "Real-time Chat Application with WebSocket and Redis",
                "E-commerce Microservices Backend with Docker",
                "AI-powered Personal Finance Tracker"
            ],
            "interview_questions": [
                "Explain the CAP theorem and its implications.",
                "How would you design a rate limiter?",
                "What is the difference between TCP and UDP?",
                "Explain how Garbage Collection works.",
                "Describe a challenging bug you fixed."
            ]
        }
