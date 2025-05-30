from fastapi import APIRouter
from pydantic import BaseModel, Field, field_validator
from datetime import date
from fastapi import Form


app05 = APIRouter()

@app05.post('/regin')
async def reg(username: str=Form(),password: str=Form()):
    print(f'username:{username},password:{password}')
    #注册 实现数据库的添加操作
    return {
        'username': username
    }