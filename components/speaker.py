import wave
import subprocess
from piper import PiperVoice

# 1) Load the voice once
voice = PiperVoice.load("../voices/de_DE-thorsten-high.onnx")

print('Geladen')

def say(text: str, filename="out.wav"):
    """Generate speech with Piper and save it to a WAV file, then play it."""
    with wave.open(filename, "wb") as wf:
        voice.synthesize_wav(text, wf)

    # 2) Play the WAV file with ALSA
    subprocess.run(["aplay", filename])

# Example:
say("Guten Morgen! Ich bin Piper und spreche jetzt direkt über die Datei.")
