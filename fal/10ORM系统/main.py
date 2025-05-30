from fastapi import FastAPI, Request
import uvicorn

from tortoise.contrib.fastapi import register_tortoise



app = FastAPI()
register_tortoise(
    app=app,
    config={
        "connections": {
            "default": {}
        }
        'apps': {
            'models': {
                'models': ['models'],
                'default_connection': 'default',
            }
        }
    }