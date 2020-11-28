import pdb
from fastapi import FastAPI
from pydantic import Json
from starlette.requests import Request
from .scripts.generator import translate

app = FastAPI()


@app.get("/")
async def convert(data: Json):
    return {"model": translate(data)}
