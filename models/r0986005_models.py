from pydantic import BaseModel
from datetime import date, datetime

class ReleaseDate(BaseModel):
    movie_name: str
    release_date: date

class LatestNews(BaseModel):
    title: str
    content: str
    published_at: datetime = None

class ContactMessage(BaseModel):
    name: str
    email: str
    subject: str
    message: str
    submitted_at: datetime = None
