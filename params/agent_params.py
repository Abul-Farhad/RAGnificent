from pydantic import BaseModel, Field
from typing import Callable, List, Optional, Any

class AgentParams(BaseModel):
    model: str
    api_key: str
    base_url: str
    system_prompt: str = 'You are a helpful AI assistant.'
    summary_prompt: str = 'You are a summarizer that condenses the conversation into a concise summary.'
    tools: Optional[List[Callable]] = Field(default_factory=list)
    thread_id: str
    user_information: Optional[dict[str, Any]] = Field(default_factory=dict)
    temperature: Optional[float] = 0.7
