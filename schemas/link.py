"""
Pydantic model for links reterived from the company's website
"""

from pydantic import BaseModel, HttpUrl
from typing import List

class Link(BaseModel):
    type: str
    link: HttpUrl  # Use str instead if the URLs might not be fully valid

class LinksResponse(BaseModel):
    links: List[Link]
