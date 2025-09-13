import uuid
import wave
import subprocess
import os
from piper import PiperVoice

os.sched_setaffinity(0, {0, 1})
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"

voice = PiperVoice.load("../voices/de_DE-thorsten-medium.onnx")

def generate_speech(text: str):
    filename = f"../generated_speech/{uuid.uuid4()}.wav"

    with wave.open(filename, "wb") as wf:
        voice.synthesize_wav(text, wf)

    return filename

def say(filename):
    subprocess.run(["aplay", filename])

def generate_and_say(text):
    say(generate_speech(text))
