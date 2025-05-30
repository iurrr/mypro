from fastapi import APIRouter
from pydantic import BaseModel, Field, field_validator
from datetime import date
from fastapi import Form, File, UploadFile
import os

app06 = APIRouter()


@app06.post('/file')
async def get_file(file: bytes=File()):
    #适合小文件上传
    print('file:', file)
    return {
        'file': len(file) #返回上传
    }
    
    
@app06.post('/files')
async def get_files(files: list[bytes]=File()):

    for file in files:  
        print(len(file))
    return {
        'files': len(files) #返回上传
    }
    
    

@app06.post('/uploadedfile')
async def get_uploadfile(file: UploadFile):

    print('file:', file)
    path = os.path.join('source', file.filename)
    #文件的保存
    with open(path, 'wb') as f:
        for line in file.file:
            f.write(line)
            
    return {
        file.filename #返回上传
    }    
    
    