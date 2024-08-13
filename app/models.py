from pydantic import BaseModel


class Student(BaseModel):
    name: str
    gender: str
    age: int
    hair: str
    glasses: bool
    career: str
