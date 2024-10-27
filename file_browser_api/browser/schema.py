from pydantic import BaseModel


class CreateFilePayload(BaseModel):
    content: str