from fastapi import FastAPI
from pydantic import BaseModel

class RenderRequest(BaseModel):
    sample_rate: int
    buffer: list[float]

app = FastAPI()

@app.post("/")
def root(render_request: RenderRequest):
    return {"Hello": "World"}