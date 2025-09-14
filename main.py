from fastapi import FastAPI
from pydantic import BaseModel

from components.buttons import TOGGLE_SWITCHES
from components.displays import DISPLAYS
from riddles.lightsout import LightsOut

app = FastAPI()


class LightsOutRequest(BaseModel):
    correctGlyph: str
    incorrectGlyph: list[str]
    introduction: str
    onFail: list[str]
    onSolve: str


@app.post("/lights_out")
async def say_hello(body: LightsOutRequest):

    l = LightsOut(
        body.correctGlyph,
        body.incorrectGlyph,
        TOGGLE_SWITCHES,
        DISPLAYS[:4],
        body.introduction,
        body.onFail,
        body.onSolve
    )
    l.start()

    print(body)
    return {"message": f"Hello"}
