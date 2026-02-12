# 🚀 CareerLens AI - How to Run

Follow these steps to get your Career Intelligence Platform up and running!

## 1. Prerequisites
- Python 3.10+
- Internet connection (for Gemini AI)
- Your `.env` file must contain a valid `GEMINI_API_KEY`

## 2. Backend Setup
The backend is built with FastAPI. To start it:

1. Open a terminal in the `backend` folder.
2. If you haven't installed dependencies yet, run:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the server using our optimized run script:
   ```bash
   python run.py
   ```
   *The server is now configured to listen on `0.0.0.0:9000`, making it accessible on your local network!*

## 3. Frontend Setup (Stitch App)
Since this is a HTML/JS app, you don't need to install anything!

1. Navigate to: `frontend/stitch/landing_page/code.html`
2. Right-click the file and select **"Open with Live Server"** (highly recommended) or double-click to open in browser.
3. Click **"Analyze My Resume"** to start the flow.
4. **Network Access**: You can also open the app on your mobile phone or another device by using your computer's IP address (e.g., `http://192.168.1.5:5500/frontend/stitch/landing_page/code.html`).

## 4. GitHub Upload Preparation
We've included a `.gitignore` file and a `.env.example`. 
> [!IMPORTANT]
> **NEVER** upload your `.env` file or API keys to GitHub. Use `.env.example` as a template for others.

## 5. Troubleshooting
- **CORS Error**: Ensure the backend is running on port **9000**.
- **AI Error**: Check your `GEMINI_API_KEY` in `backend/.env`. The system includes robust fallback data so you can always demonstrate features even offline!
- **Path Issues**: Always start from the `landing_page` to ensure the authentication and session flow works correctly.

---
**Good luck with your Hackathon presentation!** 🏆
