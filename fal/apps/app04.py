from fastapi import APIRouter
from pydantic import BaseModel, Field, field_validator
from datetime import date

app04 = APIRouter()

class Addr(BaseModel):
    city: str
    province: str

class User(BaseModel):
    name: str 
    age: int = Field(default=18, ge=0, le=150)
    birth: date | None = None
    friends: list[int] = []
    description: str | None = None
    addr: Addr

    @field_validator('name')
    def nameMustAlpha(cls,value):
        assert value.isalpha(), 'name must be alphabetic'
        return value
        
class Data(BaseModel):
    data: list[User]


@app04.post("/user")
async def user(user: User):
    return user

@app04.post('/data')
async def data(data: Data):
    return data