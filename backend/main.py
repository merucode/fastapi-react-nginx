from fastapi import FastAPI

from domain.words_count import words_count_router

app = FastAPI(root_path="/api")

@app.get("/")
async def hello():
    return {"message": "Hello World!"}

app.include_router(words_count_router.router)
