from pydantic import BaseModel, HttpUrl


class ProfileMetadata(BaseModel):
    url: HttpUrl
    price: str
    location: str
    summary: str


class Profile(BaseModel):
    text: str
    metadata: ProfileMetadata
