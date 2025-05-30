from typing import Annotated, Literal
from enum import Enum
from fastapi import FastAPI, Query, Path
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
import uvicorn

from apps.app01.urls import shop
from apps.app02.urls import user
from apps.app03 import app03
from apps.app04 import app04        
from apps.app05 import app05 
from apps.app06 import app06
from apps.app07 import app07
from apps.app08 import app08

class Item(BaseModel):
    name: str
    price: float    
    description: str | None = None
    tax: float | None = None
    
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"
    
    
app = FastAPI()


app.mount('/static', StaticFiles(directory='statics'), name='static')

app.include_router(shop, prefix="/shop", tags=["购物中心接口"])
app.include_router(user, prefix="/user", tags=["用户中心接口"])
app.include_router(app03, prefix="/job", tags=["工作信息接口"])
app.include_router(app04, tags=['请求体数据'])
app.include_router(app05, tags=['form表单数据'])
app.include_router(app06, tags=['文件上传'])
app.include_router(app07, tags=['request对象'])
app.include_router(app08, tags=['响应参数'])

class FilterParams(BaseModel):
    model_config = {"extra": "forbid"}
    
    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal['created_at', 'updated_at'] = 'created_at'
    tags: list[str] = []
    
    
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

@app.put('/items/{item_id}')
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result

@app.get("/")   
async def root():
    return {"message": "Hello World"}

@app.get('/items')
async def read_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]

@app.get("/items/")
async def read_items(filter_query: Annotated[FilterParams, Query()]):
    return filter_query

""" @app.get('/items/{item_id}')
async def read_items(
    *,
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: str,
    size: Annotated[float, Query(gt=0, lt=10.5)],
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if size:
        results.update({"size": size})
    return results """
    
    
@app.get('/users/me')
async def read_user_me():   
    return {'user_id': "the current user"}

@app.get('/users/{user_id}')
async def read_user(user_id: int):
    return {'user_id': user_id} 

@app.get("/users/{user_id}/items/{item_id}" )
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {'description': '这是个有很长描述的description'}  
        )  
    return item

@app.get('/models/{model_name}')    
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {'model_name':model_name, 'message': '1111abbb'}
    
    if model_name.value == 'lenet':
        return {'model_name':model_name, 'message': '哈哈哈哈东方东方'}
    
    return {'model_name':model_name, 'message': '吃点剩饭'}


@app.get('/files/{file_path:path}')
async def read_file(file_path: str):
    return {'file_path': file_path}

@app.post('/test',tags=['这是post接口测试'],
          summary='关于post测试的summary',
          description='关于post测试的description',
          response_description='关于post测试的response_description'
          )
def test():
    return {'message': 'test'}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)