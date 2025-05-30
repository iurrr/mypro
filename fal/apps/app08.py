from fastapi import APIRouter, Request
from pydantic import BaseModel, EmailStr
from datetime import date
import os

app08 = APIRouter()



class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr | None = None    
    full_name: str | None = None
    
    
class UserOut(BaseModel):
    username: str
    email: EmailStr | None = None    
    full_name: str | None = None
    
    
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.5
    tags : list[str] = []
    
items = {
    'foo': {'name': 'foo', 'price': 50.2},
    'bar': {'name': 'bar', 'description': 'A very nice bar', 'price': 62, 'tax': 10.5, 'tags': ['vegetarian']},
    'baz': {'name': 'baz', 'description': 'A very nice baz', 'price': 55.5, 'tax': 20.9, 'tags': ['vegan', 'gluten-free']}
}
    
@app08.post('/user_reg', response_model=UserOut)
def create_user(user: UserIn):
    #存到数据库
    return user


@app08.get('/items/{item_id}', response_model=Item, response_model_include={'name', 'description'})
async def read_item(item_id: str):
    return items[item_id]
    