from fastapi import FastAPI
from routers import contact

app = FastAPI()

# @app.get("/")
# async def root():
#     return { "message": "Hello World"}

app.include_router(contact.router)