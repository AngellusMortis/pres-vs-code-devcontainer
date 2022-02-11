import aioredis
from fastapi import FastAPI
from pydantic import BaseModel, BaseSettings, PrivateAttr


class Config(BaseSettings):
    redis_url: str = "redis://redis:6379/0"


class Redis(BaseModel):
    config: Config
    _client: aioredis.Redis | None = PrivateAttr(None)

    @property
    def client(self) -> aioredis.Redis:
        if self._client is None:
            self._client = aioredis.from_url(config.redis_url, decode_responses=True)  # type: ignore

        return self._client


class Stuff(BaseModel):
    message: str
    count: int


config = Config()
app = FastAPI()
redis = Redis(config=config)


@app.get("/healthcheck/")
async def healthcheck() -> str:
    return ""


@app.get("/", response_model=Stuff)
async def root() -> Stuff:
    return Stuff(message="Good News Everyone!", count=await redis.client.incr("count"))
