import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


""" @app.middleware("http")
async def CorMiddleware(request: Request, call_next):
    response = await call_next(request)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response """
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['get','post'],
    allow_headers=['*'],
)

@app.get('/user')
def getUser():
    
    return {
        "name": "张三"
    }



if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)