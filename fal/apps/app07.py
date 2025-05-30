from fastapi import APIRouter, Request
from pydantic import BaseModel, Field
from datetime import date
from fastapi import Form, File, UploadFile
import os

app07 = APIRouter()


@app07.post('/request')
async def get_request(request: Request):    
    print('url:', request.url)
    print('客户端IP：', request.client.host)
    print('客户端端口：', request.client.port)
    print('请求头：', request.headers)
    print('客户端宿主：', request.headers.get('user-agent'))
    print('请求方法：', request.method)
    print('请求参数：', request.query_params)
    
    return {
        'url': request.url,
        '客户端IP': request.client.host,
        '客户端端口': request.client.port,
        '请求头': request.headers,
        '客户端宿主': request.headers.get('user-agent'),
        '请求方法': request.method,
        '请求参数': request.query_params,
        'cookie': request.cookies
    }  