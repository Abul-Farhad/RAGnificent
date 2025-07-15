from pydantic import BaseModel, Field
from typing import Callable, List, Optional, Any

class AgentParams(BaseModel):
    groq_model: str
    groq_api_key: str
    system_prompt: str = 'You are a helpful AI assistant.'
    summary_prompt: str = 'You are a summarizer that condenses the conversation into a concise summary.'
    tools: Optional[List[Callable]] = Field(default_factory=list)
    thread_id: int
    user_information: Optional[dict[str, Any]] = Field(default_factory=dict)
