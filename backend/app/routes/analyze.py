from fastapi import APIRouter, UploadFile, File, Form, Body
from app.services.resume_parser import extract_text_from_pdf
from app.services.skill_extractor import extract_skills_from_resume
from app.services.rag_retriever import get_role_skills
from app.services.gap_analyzer import analyze_skill_gap
from app.services.roadmap_generator import generate_roadmap
from app.services.interview_mentor import evaluate_interview_answer
from app.services.chatbot_service import get_chatbot_response

router = APIRouter()

@router.post("/chatbot")
async def chatbot_respond(
    payload: dict = Body(...)
):
    message = payload.get("message", "")
    context = payload.get("context", {}) # New: target_role, score, missing_skills
    
    if not message:
        return {"error": "Message is required"}
    
    response = get_chatbot_response(message, context)
    return {"response": response}

@router.post("/analyze")
async def analyze_resume(
    resume: UploadFile = File(...),
    target_role: str = Form(...)
):
    try:
        # 1. Extract text from PDF
        text = extract_text_from_pdf(resume.file) or ""

        if not str(text).strip():
            return {
                "error": "Resume text could not be extracted properly."
            }

        # 2. Get required skills for the role
        role_skills = get_role_skills(target_role)

        # 3. Extract skills using AI (Gemini)
        extracted = extract_skills_from_resume(text, role_skills)
        technical_skills = extracted.get("technical_skills", [])

        # 4. Perform structured Gap Analysis
        gap_analysis = analyze_skill_gap(technical_skills, role_skills)

        # 5. Generate Actionable Roadmap using AI
        roadmap = generate_roadmap(
            target_role,
            gap_analysis["missing_skills"]
        )

        # Propagate 'is_partial' if any service hit a fallback
        is_partial = any([
            extracted.get("is_partial", False),
            gap_analysis.get("is_partial", False),
            roadmap.get("is_demo_mode", False) or roadmap.get("api_error", False)
        ])
        gap_analysis["is_partial"] = is_partial

        return {
            "target_role": target_role,
            "technical_skills": technical_skills,
            "role_required_skills": role_skills,
            "gap_analysis": gap_analysis,
            "roadmap": roadmap
        }
    except Exception as e:
        print(f"CRITICAL ANALYZE ERROR: {str(e)}")
        # Return a graceful failure structure
        return {
            "error": "The AI service is currently overloaded. Please try again in 30 seconds.",
            "details": str(e),
            "is_partial": True
        }

@router.post("/feedback")
async def get_interview_feedback(
    payload: dict = Body(...)
):
    question = payload.get("question", "")
    answer = payload.get("answer", "")
    target_role = payload.get("target_role", "Candidate")
    
    if not question or not answer:
        return {"error": "Question and answer are required"}
        
    feedback = evaluate_interview_answer(question, answer, target_role)
    return feedback
