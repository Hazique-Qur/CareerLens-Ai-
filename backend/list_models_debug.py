import os
import sys
import google.generativeai as genai

# Add backend to path
sys.path.append(os.path.join(os.getcwd(), 'app'))
from app.utils.config import GEMINI_API_KEY

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    print("Listing available models...")
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
else:
    print("No API Key found.")
