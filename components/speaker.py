import subprocess
import shlex

def say_de(text: str, speed_wpm=160, pitch=40, volume=80):
    # -v de  -> German voice
    # -s     -> speed (words per minute)
    # -p     -> pitch (0–99)
    # -a     -> volume/amplitude (0–200)
    cmd = f'espeak-ng -v de -s {speed_wpm} -p {pitch} -a {volume} {shlex.quote(text)}'
    subprocess.run(cmd, shell=True, check=True)

if __name__ == "__main__":
    say_de("Hallo! Ich spreche Deutsch auf deinem Raspberry Pi.")