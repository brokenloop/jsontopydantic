from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Json
from starlette.requests import Request
from typing import Dict, Any
from mangum import Mangum

from .scripts.generator import translate


app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)


class BasicRequest(BaseModel):
    data: Json


@app.post("/")
async def convert(basicRequest: BasicRequest):
    return {"model": translate(basicRequest.data)}


handler = Mangum(app)