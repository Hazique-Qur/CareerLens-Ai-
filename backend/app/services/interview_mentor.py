import google.generativeai as genai
from app.utils.config import GEMINI_API_KEY
import json

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

def evaluate_interview_answer(question: str, answer: str, target_role: str = "Candidate"):
    if not GEMINI_API_KEY:
        return {
            "score": 7,
            "feedback_title": "Simulated Feedback",
            "feedback_summary": "Gemini API key missing. Providing simulated feedback.",
            "strengths": ["Clear communication"],
            "improvements": ["Provide more technical examples"]
        }

    model = genai.GenerativeModel("models/gemini-1.5-pro-latest")
    
    prompt = f"""
    You are an expert technical interviewer for a {target_role} position. 
    Evaluate the candidate's answer to the following question specifically for the role of {target_role}.
    
    Question: {question}
    Answer: {answer}
    
    CRITICAL EVALUATION RULES:
    1. If the answer is gibberish, nonsensical (e.g., 'asdf', 'huaoboueva'), or completely unrelated to the technical topic, YOU MUST give a score of 0 or 1.
    2. If the user says they don't know, give a low score (1-2) but acknowledge the honesty.
    3. Do not be overly polite. Be a critical, professional interviewer.
    4. If the role is 'Senior', look for architectural depth and trade-offs. 
    5. If it's 'Junior', look for core conceptual understanding.

    Return output strictly in this JSON format:
    {{
        "score": (integer 0-10),
        "feedback_title": (string, brief e.g., "Incoherent Response" or "Strong Technical Depth"),
        "feedback_summary": (string, 1-2 sentences overview),
        "strengths": [(string), (string)],
        "improvements": [(string), (string)],
        "confidence_score": (integer 0-100 indicating how confident the answer sounded)
    }}
    """

    try:
        response = model.generate_content(prompt)
        text_response = response.text.replace("```json", "").replace("```", "").strip()
        return json.loads(text_response)
    except Exception as e:
        print(f"Interview Mentor AI Error: {str(e)}")
        # Safe Fallback - Don't give fake high scores
        return {
            "score": 0,
            "feedback_title": "AI Service Unavailable",
            "feedback_summary": "We couldn't analyze your response at this moment. Please check your internet connection and try again.",
            "strengths": ["Analysis failed"],
            "improvements": ["Try resubmitting your answer"],
            "confidence_score": 0
        }
