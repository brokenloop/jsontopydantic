from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Json, Field
from mangum import Mangum

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
    options: Options


@app.post("/")
async def convert(basic_request: BasicRequest):
    return {
        "model": translate(
            basic_request.data,
            basic_request.options.force_optional,
            basic_request.options.snake_cased,
        )
    }


handler = Mangum(app)
