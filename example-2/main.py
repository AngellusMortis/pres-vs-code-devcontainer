import aioredis
from fastapi import FastAPI
from pydantic import BaseSettings, BaseModel


class Config(BaseSettings):
    redis_url: str = 'redis://redis:6379'


config = Config()
app = FastAPI()
redis = aioredis.from_url(config.redis_url, decode_responses=True)


class Stuff(BaseModel):
    message: str
    count: int


@app.get("/healthcheck/")
async def healthcheck() -> str:
    return ""


@app.get("/", response_model=Stuff)
async def root() -> Stuff:
    return Stuff(message="Good News Everyone!", count=await redis.incr("count"))
