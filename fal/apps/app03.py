from fastapi import APIRouter

app03 = APIRouter()

@app03.get("/{kd}")
async def getJob(kd, xl: str | None =None, gj=None): #xl和gj可选参数
    
    #基于3个参数数据库查询，返回工作信息      
    return {
        'kd': kd,
        'xl': xl,
        'gj': gj
    }