import google.generativeai as genai
from app.utils.config import GEMINI_API_KEY

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

def get_chatbot_response(message: str):
    if not GEMINI_API_KEY:
        return "I'm currently in offline mode. Please configure the Gemini API key to enable full AI capabilities."

    model = genai.GenerativeModel("models/gemini-1.5-flash-latest")
    
    system_prompt = """
    You are the CareerLens AI Senior Career Advisor. You help users navigate their career transitions and platform features.
    
    PLATFORM CAPABILITIES:
    - Resume Analysis: Deep scan of technical DNA and market alignment.
    - 100-Day Roadmap: 5-step detailed plan with specific resources and milestones.
    - Interview Simulator: Voice-powered (TTS/STT) practice with real-time feedback.
    - Live Job Search: Dynamic link generation for LinkedIn, Indeed, Glassdoor.
    - Pro Plan ($19): Unlimited analyses, premium roadmaps, and priority mentor access.

    STRICT OPERATIONAL GUIDELINES:
    1. ANALYTICAL FILTER: If a message is nonsensical, gibberish (e.g., 'asdf', 'test'), or a "wrong question", DO NOT provide a standard technical answer. Politely ask for clarification.
    2. CAREER SCOPE: Only answer questions related to careers, tech skills, jobs, and CareerLens AI. Politely refuse everything else (e.g., "I'm a career expert, not a chef/historian/etc.").
    3. TONE: Professional, slightly formal but encouraging, and data-driven.
    4. CONTEXT: If the user asks general career advice, lean into the platform's features (e.g., "You should use our Roadmap feature for that").
    """

    try:
        chat = model.start_chat(history=[])
        response = chat.send_message(f"{system_prompt}\n\nUser Message: {message}")
        return response.text
    except Exception as e:
        print(f"Chatbot AI Error: {str(e)}")
        return "I'm sorry, I'm having trouble processing that right now. Could you try rephrasing your question?"
