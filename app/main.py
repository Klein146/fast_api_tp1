from fastapi import FastAPI
from routes.router_main import router as router_main
import uvicorn

app = FastAPI(title="TODO API", version="1.0.0")

app.include_router(router_main)

@app.get("/")
def info():
    return {"api": "rest api"}

if __name__ == "__main__":
    uvicorn.run('main:app', host="localhost", port=8000, reload=True)
