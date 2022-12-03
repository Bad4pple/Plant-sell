from fastapi import FastAPI
from rest.routers import router

app = FastAPI()

app.include_router(router=router)