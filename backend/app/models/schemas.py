from pydantic import BaseModel
from typing import List, Optional

class AnalysisRequest(BaseModel):
    resume_text: str
    job_description: Optional[str] = None

class AnalysisResponse(BaseModel):
    skills: List[str]
    gaps: List[str]
    roadmap: List[str]
