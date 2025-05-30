from fastapi import FastAPI, Request
import uvicorn
from fastapi.responses import Response


app = FastAPI()

@app.middleware("http")
async def m2(request: Request, call_next):
    #请求代码块
    print("m2请求代码块")
    response = await call_next(request)
    #响应代码块
    response.headers['author'] = 'rui'
    print("m2响应代码块")
    
    return response


@app.middleware("http")
async def m1(request: Request, call_next):
    #请求代码块
    print("请求代码块")
    if request.client.host == '127.0.0.1':
        print("请求来自本地")
        return Response(content="not allowed", status_code=403)
    response = await call_next(request)
    #响应代码块
    print("响应代码块")
    
    return response

@app.get("/user")
def getUser():
    print("getUser函数执行")
    return {
        "name": "张三"
    }
    
@app.get("/items/{item_id}")
def getItem(item_id: int):
    print("getItem函数执行")
    return {
        "item_id": item_id
    }


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)