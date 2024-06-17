from pydantic import BaseModel, Field


class TextToSummarizeSchema(BaseModel):
    text: str = Field(examples=["Some text"])
