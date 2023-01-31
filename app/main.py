from fastapi import FastAPI
from router.router import service

app = FastAPI()

app.include_router(service)