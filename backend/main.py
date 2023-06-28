from fastapi import FastAPI

from domain.test import test_router

app = FastAPI(root_path="/api")

@app.get("/")
def hello():
    return {"message": "Hello World!"}

app.include_router(test_router.router)
