import random
from signal import pause
from time import sleep
from gpiozero import Button

from components.buttons import TOGGLE_SWITCHES
from components.displays import Display, DISPLAYS
from components.neopixels import NEOPIXELS


CHECKMARK_PATH = "../assets/checkmark.png"


class LightsOut:
    def __init__(self, correct_glyph, incorrect_glyph: list[str], toggles: list[Button], displays: list[Display]):
        self.correct_glyph = correct_glyph
        self.incorrect_glyph = incorrect_glyph
        self.buttons = toggles
        self.displays = displays
        self.running = True
        self.state = [False] * 4
        self.wiring = create_wiring()

    def switch(self, switch_number):
        for i, b in enumerate(self.wiring[switch_number]):
            if b:
                self.state[i] = not self.state[i]
                self.update_display(i)
        if self.is_solved():
            self.handle_solved()

    def update_display(self, display_number):
        if (self.state[display_number]):
            glyph = self.correct_glyph
        else:
            glyph = self.incorrect_glyph[display_number]
        self.displays[display_number].show_hieroglyph(glyph)

    def start(self):
        NEOPIXELS.start_continuous(0.7)
        for i in range(4):
            self.buttons[i].when_activated = lambda i=i: self.switch(i)
            self.buttons[i].when_deactivated = lambda i=i: self.switch(i)
            self.update_display(i)

    def stop(self):
        for i in range(4):
            self.displays[i].show_asset(CHECKMARK_PATH)
            self.buttons[i].when_activated = None
            self.buttons[i].when_deactivated = None

    def is_solved(self):
        return all(self.state)

    def handle_solved(self):
        if not self.is_solved():
            return
        self.stop()
        NEOPIXELS.start_continuous(0.3)

def create_wiring() -> list[list[bool]]:
    rng = random.Random()
    base = [
        [True, True, False, False],
        [True, True, True, False],
        [False, True, True, True],
        [False, False, True, True]
    ]

    # Apply the same permutation  to row and columns, so that diagnol stays the same (all true, such that each toggle
    # switch switches its own display)
    p = list(range(4))
    rng.shuffle(p)
    M = [[base[p[i]][p[j]] for j in range(4)] for i in range(4)]
    return M


i = LightsOut('Owl', ['Lion', 'Man_standing', 'Elephant', 'Scarab'], TOGGLE_SWITCHES[:4], DISPLAYS[:4])
i.start()
pause()
