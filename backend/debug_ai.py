import os
import sys
import traceback

# Add backend to path
sys.path.append(os.path.join(os.getcwd(), 'app'))

from app.utils.config import GEMINI_API_KEY
import google.generativeai as genai

print(f"API Key present: {bool(GEMINI_API_KEY)}")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

try:
    print("Attempting to call models/gemini-1.5-pro-latest...")
    model = genai.GenerativeModel("models/gemini-1.5-pro-latest")
    response = model.generate_content("Say hello")
    print("Direct Response:", response.text)
except Exception:
    traceback.print_exc()
