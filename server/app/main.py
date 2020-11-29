import pdb
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from starlette.requests import Request
from typing import Dict, Any
from .scripts.generator import translate


class BasicRequest(BaseModel):
    data: Dict[Any, Any]


app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)

@app.post("/")
async def convert(basicRequest: BasicRequest):
    # return {"model": translate(request.data)}
    return {"model": "lol"}
