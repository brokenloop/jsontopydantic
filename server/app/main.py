import pdb
import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Json
from starlette.requests import Request
from typing import Dict, Any
from .scripts.generator import translate


logger = logging.getLogger(__name__)


class BasicRequest(BaseModel):
    data: Json


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


@app.get("/testget")
async def testget():
    return {"model": "success"}


@app.post("/")
async def convert(basicRequest: BasicRequest):
    return {"model": translate(basicRequest.data)}
