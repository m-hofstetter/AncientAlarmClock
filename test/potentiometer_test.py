from time import sleep

from components.displays import DISPLAYS
from components.potentiometers import Potentiometers


pots = Potentiometers()

while True:
    DISPLAYS[8].write(f"{pots.get_percent(0):.1f}")
    DISPLAYS[9].write(f"{pots.get_percent(1):.1f}")
    DISPLAYS[10].write(f"{pots.get_percent(2):.1f}")