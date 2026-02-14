import google.generativeai as genai
from app.utils.config import GEMINI_API_KEY

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

def get_chatbot_response(message: str, context: dict = None):
    if not GEMINI_API_KEY:
        return "Offline mode active. Configure GEMINI_API_KEY for live career strategy."

    model = genai.GenerativeModel("models/gemini-2.0-flash")
    
    # Enhanced Context Injection
    context_str = "USER CONTEXT: "
    if context:
        role = context.get('role', 'Ambassador')
        score = context.get('score', 'N/A')
        missing = ", ".join(context.get('missing_skills', []))
        level = context.get('experience_level', 'Professional')
        context_str += f"Targeting {role}, Current Match: {score}%, Skill Level: {level}. Missing: [{missing}]."
    else:
        context_str += "New visitor exploring the platform."

    system_prompt = f"""
    You are the CareerLens Senior Career Strategist. You provide elite, data-driven advice.
    
    {context_str}

    STRATEGIC OBJECTIVES:
    1. BE AGENTIC: Don't just answer; suggest the next step in their roadmap or a specific project.
    2. INDUSTRY INSIGHT: Use modern tech industry context (e.g., mention MLOps for AI roles, or SSR for Frontend).
    3. PLATFORM MASTERY: Reference "Skill Radar", "100-Day Roadmap", and "Interview Simulator" as tools they should use.
    4. TONALITY: Authoritative yet inspiring. Think 'Silicon Valley Mentor'.
    
    STRICT RULES:
    - If the user asks something non-career related, pivot back to their career or politely decline.
    - If the user provides gibberish, respond: "To provide an elite career strategy, I need clear input. How can I help you pivot today?"
    - Keep responses concise but high-impact.
    """

    try:
        chat = model.start_chat(history=[])
        response = chat.send_message(f"{system_prompt}\n\nUser Message: {message}")
        return response.text
    except Exception as e:
        print(f"Chatbot AI Error: {str(e)}")
        return "I'm optimizing my processing nodes. Try again in 10 seconds."
