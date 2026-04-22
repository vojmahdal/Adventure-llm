from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field


class StoryOptionLLM(BaseModel):
    text: str = Field(description="The text of the options shown to the user")
    nextNode: Dict[str, Any] = Field(description="Next node content and its options")

class StoryNodeLLM(BaseModel):
    content: str = Field(description="The main content of the story mode")
    isEnding: bool = Field(description="Whether the story is ending or not")
    isWinningEnding: bool = Field(description="Whether the story is winning or not")
    options: Optional[List[StoryOptionLLM]] = Field(default=None, description="The options shown to the user")

class StoryLLMResponse(BaseModel):
    title: str = Field(description="The title of the story")
    rootNode: StoryNodeLLM = Field(description="The root node of the story")
