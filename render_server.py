from fastapi import FastAPI
from fastapi.openapi.models import Response
from pydantic import BaseModel
from fastapi.responses import HTMLResponse, FileResponse
from analyzer import PPAAnalyzer


class RenderRequest(BaseModel):
    sample_rate: int
    buffer: list[float]

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def root_get():
    return """
        <center>
            This is the render server of PyPublicAdress! To render a file send a json with the fields sample_rate and buffer containing a list of floats!
            <br>
            <br>{ \"sample_rate\": 48000, \"buffer\": [1, -1, 1, -1, 1, -1, 1, -1, 1] }
        </center>
    """

@app.post("/")
def root(render_request: RenderRequest):
    a = PPAAnalyzer()
    fn = a.analyze(buffer=render_request.buffer, sample_rate=render_request.sample_rate)
    return FileResponse(fn, media_type="image/png")
    #return {"fn": fn}