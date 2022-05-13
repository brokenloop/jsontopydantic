from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Json, Field
from mangum import Mangum
from typing import Optional

from .scripts.generator import translate


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)


class Options(BaseModel):
    force_optional: bool = Field(False, alias="forceOptional")
    snake_cased: bool = Field(False, alias="snakeCased")


class BasicRequest(BaseModel):
    data: Json
    options: Optional[Options]


@app.post("/")
async def convert(basic_request: BasicRequest):
    print(basic_request)
    options = basic_request.options if basic_request.options is not None else Options()
    return {
        "model": translate(
            basic_request.data,
            options.force_optional,
            options.snake_cased,
        )
    }


handler = Mangum(app)
