# python
from pydantic import BaseModel

class ResearchResponse(BaseModel):
    title: str
    summary: str
    source: str
    tools_used: list[str]