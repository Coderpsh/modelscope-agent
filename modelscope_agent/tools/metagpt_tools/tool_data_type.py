# this code is originally from https://github.com/geekan/MetaGPT
from pydantic import BaseModel
from typing import List


class ToolSchema(BaseModel):
    description: str


class Tool(BaseModel):
    name: str
    path: str
    schemas: dict = {}
    code: str = ''
    tags: List[str] = []
