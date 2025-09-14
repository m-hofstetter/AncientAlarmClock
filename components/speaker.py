import os
import uuid
import wave

import pygame
from gtts import gTTS
from piper import PiperVoice

os.sched_setaffinity(0, {0, 1})
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"

voice = PiperVoice.load("./voices/de_DE-thorsten-medium.onnx")

pygame.mixer.init()
SUCCESS_SOUND = pygame.mixer.Sound("./assets/success.mp3")


def generate_speech(text: str, local=False):
    if local:
        filename = f"./generated_speech/{uuid.uuid4()}.wav"
        with wave.open(filename, "wb") as wf:
            voice.synthesize_wav(text, wf)
    else:
        filename = f"./generated_speech/{uuid.uuid4()}.mp3"
        tts = gTTS(text=text, lang='de')
        tts.save(filename)

    return filename


def say(filename):
    sound = pygame.mixer.Sound(filename)
    sound.play()


def generate_and_say(text):
    say(generate_speech(text))
