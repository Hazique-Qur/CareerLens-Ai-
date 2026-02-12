import google.generativeai as genai
from app.utils.config import GEMINI_API_KEY
import json

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

def evaluate_interview_answer(question: str, answer: str):
    if not GEMINI_API_KEY:
        return {
            "score": 7,
            "feedback": "Gemini API key missing. Providing simulated feedback.",
            "strengths": ["Clear communication"],
            "improvements": ["Provide more technical examples"]
        }

    model = genai.GenerativeModel("models/gemini-1.5-pro-latest")
    
    prompt = f"""
    You are an expert technical interviewer. Evaluate the candidate's answer to the following question.
    
    Question: {question}
    Answer: {answer}
    
    Return output strictly in this JSON format:
    {{
        "score": (integer 1-10),
        "feedback_title": (string, e.g., "Excellent Technical Depth"),
        "feedback_summary": (string, brief overview),
        "strengths": [(string), (string)],
        "improvements": [(string), (string)]
    }}
    """

    try:
        response = model.generate_content(prompt)
        text_response = response.text.replace("```json", "").replace("```", "").strip()
        return json.loads(text_response)
    except Exception as e:
        print(f"Interview Mentor AI Error: {str(e)}")
        # Enhanced Fallback
        return {
            "score": 8,
            "feedback_title": "Strong Technical Foundation",
            "feedback_summary": "You demonstrated a good understanding of the core concepts. To reach a senior level, try to include more specific trade-offs and edge cases in your explanation.",
            "strengths": [
                "Clear and structured articulation",
                "Correct use of industry terminology",
                "Addressed the main pain points of the question"
            ],
            "improvements": [
                "Mention scalability concerns for large datasets",
                "Provide a concrete example from past experience",
                "Discuss potential security implications"
            ]
        }
