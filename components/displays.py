from time import sleep

import adafruit_ssd1306
import adafruit_tca9548a
import board
import busio
from board import I2C

from components.imagegenerator import ImageGenerator

DISPLAY_I2C_ADDRESS = 0x3C
OLED_WIDTH, OLED_HEIGHT = 128, 64

MAX_CONNECTION_TRIES = 5

class Display:

    def __init__(self, i2c: I2C):
        self.__i2c = i2c
        self.__text_image_generator = ImageGenerator()
        self._init_display()

    def _init_display(self):
        for attempt in range(MAX_CONNECTION_TRIES):  # try twice
            try:
                # give mux channel time to settle
                self.__oled = adafruit_ssd1306.SSD1306_I2C(
                    OLED_WIDTH, OLED_HEIGHT, self.__i2c,
                    addr=DISPLAY_I2C_ADDRESS
                )
                return
            except Exception as e:
                if attempt == MAX_CONNECTION_TRIES:
                    raise e  # wait a bit and retry
                else:
                    sleep(0.05)

    def show_text(self, text):
        img = self.__text_image_generator.generate_text_image(text)
        self.__oled.image(img)
        self.__oled.show()


i2c = busio.I2C(board.SCL, board.SDA)

MULTIPLEXERS = [
    adafruit_tca9548a.TCA9548A(i2c, address=0x70),
    adafruit_tca9548a.TCA9548A(i2c, address=0x71)
]

DISPLAYS = [
    Display(MULTIPLEXERS[0][3]),
    Display(MULTIPLEXERS[0][4]),
    Display(MULTIPLEXERS[0][5]),
    Display(MULTIPLEXERS[0][6]),
    Display(MULTIPLEXERS[0][2]),
    Display(MULTIPLEXERS[0][1]),
    Display(MULTIPLEXERS[0][0]),
    Display(MULTIPLEXERS[0][7]),
    Display(MULTIPLEXERS[1][5]),
    Display(MULTIPLEXERS[1][6]),
    Display(MULTIPLEXERS[1][3])
]
