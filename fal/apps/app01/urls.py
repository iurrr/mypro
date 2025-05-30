from fastapi import APIRouter

shop = APIRouter()

@shop.get("/food")
def shop_food():
    return {"food": "good"}