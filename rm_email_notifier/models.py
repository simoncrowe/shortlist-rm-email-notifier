from pydantic import BaseModel


class ProfileMetadata(BaseModel):
    url: str
    price: str
    location: str
    summary: str


class Profile(BaseModel):
    text: str
    metadata: ProfileMetadata
