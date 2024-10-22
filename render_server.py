from fastapi import FastAPI
from fastapi.openapi.models import Response
from pydantic import BaseModel

from analyzer import PPAAnalyzer


class RenderRequest(BaseModel):
    sample_rate: int
    buffer: list[float]

app = FastAPI()

@app.post("/")
def root(render_request: RenderRequest):
    a = PPAAnalyzer()
    fn = a.analyze(buffer=render_request.buffer, sample_rate=render_request.sample_rate)
    in_file = open(fn, "rb")
    image = in_file.read()
    return Response(content=image, media_type="image/png")
    #return {"fn": fn}