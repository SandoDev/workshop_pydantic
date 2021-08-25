from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """
    Root of host
    """
    return {"message": "FastAPI test"}
