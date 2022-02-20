from fastapi import FastAPI

from dotenv import load_dotenv
load_dotenv()

from .routers import health, predict
from .utils import config

app = FastAPI(title=config.title, version=config.version)
app.include_router(health.router)
app.include_router(predict.router)