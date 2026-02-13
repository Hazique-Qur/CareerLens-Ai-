import google.generativeai as genai
from app.utils.config import GEMINI_API_KEY

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

def get_chatbot_response(message: str, context: dict = None):
    if not GEMINI_API_KEY:
        return "I'm currently in offline mode. Please configure the Gemini API key to enable full AI capabilities."

    model = genai.GenerativeModel("models/gemini-flash-latest")
    
    # 1. Build Context String
    context_str = ""
    if context:
        role = context.get('role', 'Career Explorer')
        score = context.get('score', 'N/A')
        missing = ", ".join(context.get('missing_skills', []))
        context_str = f"USER CONTEXT: Target Role: {role}, Match Score: {score}%, Missing Skills: [{missing}]."

    system_prompt = f"""
    You are the CareerLens AI Senior Career Advisor. You help users navigate their career transitions and platform features.
    
    {context_str}

    PLATFORM CAPABILITIES:
    - Resume Analysis: Deep scan of technical DNA and market alignment.
    - 100-Day Roadmap: 5-step detailed plan with specific resources and milestones.
    - Interview Simulator: Voice-powered (TTS/STT) practice with real-time feedback.
    - Live Job Search: Dynamic link generation for LinkedIn, Indeed, Glassdoor.
    - Pro Plan ($19): Unlimited analyses, premium roadmaps, and priority mentor access.

    STRICT OPERATIONAL GUIDELINES:
    1. ANALYTICAL FILTER: If a message is nonsensical, gibberish (e.g., 'asdf', 'test'), or a "wrong question", DO NOT provide a standard technical answer. Politely ask for clarification.
    2. CAREER SCOPE: Only answer questions related to careers, tech skills, jobs, and CareerLens AI. Politely refuse everything else.
    3. PERSONALIZATION: If context is provided, use it! Mention their target role or suggest how to bridge their specific missing skills.
    4. TONE: Professional, slightly formal but encouraging, and data-driven.
    """

    try:
        chat = model.start_chat(history=[])
        response = chat.send_message(f"{system_prompt}\n\nUser Message: {message}")
        return response.text
    except Exception as e:
        print(f"Chatbot AI Error: {str(e)}")
        return "I'm sorry, I'm having trouble processing that right now. Could you try rephrasing your question?"
