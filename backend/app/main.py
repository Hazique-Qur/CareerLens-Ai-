from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from app.routes.analyze import router as analyze_router

load_dotenv()

app = FastAPI(
    title="CareerLens AI",
    description="AI-Powered Career Intelligence Platform",
    version="1.0.0"
)

# Enable CORS (Ultra-Permissive for Local Dev)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False, # Set to False for wildcard support
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analyze_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "CareerLens AI backend is running"}
