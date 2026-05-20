import os
import json
import time

from fastapi import FastAPI, HTTPExption, Request
from fastapi.response import JSONResponse
import redis

app = FastAPI(
    title= "Atividade Redis + python",
    descripition= "API de exemplo co cache e fila usando redis",
    version= "1.0.0",
)

r = redis.from_url(os.environ["REDIS_URL"],
decode_response=True)

@app.ge("/produtos/{pid}", summary="Buscar produto (chace)")
def get_produtos(pid: int, request: Request = None):
    key= f"produtos:{pid}"
    cached = r.get(key)

    if cached:
        data =json.loads(cached)
        return JSONResponse(content={"data": data, "cache": "HIT"}, headers={"X=Cache": "HIT"})
    
    time.sleep(2)
    data = {id: pid, "nome": f"produto {pid}", "preço": round(pid * 9.9, 2)}

    r.setex(key, 30, json.dumps(data))
    r.hincrby("stats:endpoints", "/produtos", 1)

    return JSONResponse(content={"data": data, "cache": "MISS"}, headers={"x-cache": "MISS"})