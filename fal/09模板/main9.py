from fastapi import FastAPI, Request
import uvicorn
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory='templates')
@app.get('/index')
def index(request: Request):
    name = 'root'
    books = [{'title':'book1','price':100}, 
             {'title':'book2','price':10}, 
             {'title':'book3','price':150}]
    info = {'name': 'admin', 'age': 11}
    pi = 3.1415926
    
    movies = {'cn':['日韩', '欧美', '港台'],
              'wcn':['动画片', '喜剧片', '爱情片']}
    
    return templates.TemplateResponse(
        'index.html',  #模板文件
        {
            'request': request,
            'user': name,
            'books': books,
            'info': info,
            'pi': pi,
            'movies': movies
            }  #context上下文对象，一个字典
    )


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)