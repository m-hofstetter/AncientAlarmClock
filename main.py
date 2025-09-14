from fastapi import FastAPI
from pydantic import BaseModel

from components.buttons import TOGGLE_SWITCHES
from components.displays import DISPLAYS
from riddles.lightsout import LightsOut

app = FastAPI()


class LightsOutRequest(BaseModel):
    correctGlyph: str
    incorrectGlyph: list[str]


@app.post("/lights_out")
async def say_hello(body: LightsOutRequest):

    l = LightsOut(
        body.correctGlyph,
        body.incorrectGlyph,
        TOGGLE_SWITCHES,
        DISPLAYS[:4]
    )
    l.start()

    print(body)
    return {"message": f"Hello"}
