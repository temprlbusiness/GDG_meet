from fastapi import FastAPI
from typing import Dict

app = FastAPI(
    title="Simple FastAPI Server",
    description="A basic FastAPI server with a simple endpoint",
    version="1.0.0"
)

@app.get("/")
async def root() -> Dict[str, str]:
    return {"message": "Hello World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
