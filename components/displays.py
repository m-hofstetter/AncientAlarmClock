import random

import smbus2
import adafruit_ssd1306
import board, busio
from PIL import ImageDraw, ImageFont, Image

DISPLAY_I2C_ADDRESS = 0x3C

OLED_WIDTH = 128
OLED_HEIGHT = 64

HIEROGLYPHS = {
    "Man_standing": "𓀀",
    "Seated_woman": "𓀁",
    "Seated_deity": "𓀭",
    "Owl": "𓅓",
    "Quail_chick": "𓅪",
    "Horned_ox": "𓃜",
    "Lion": "𓃭",
    "Cobra": "𓆗",
    "Reed_leaf": "𓇋",
    "Sun_disk": "𓇳",
    "Water_lines": "𓈗",
    "Placenta": "𓐍",
    "Sickle": "𓌳",
    "Penis": "𓂸",
    "Elephant": "𓃰",
    "Scarab": "𓆣"
}


class Display:
    def __init__(self, multiplexer, channel):
        self.bus = smbus2.SMBus(1)
        i2c = busio.I2C(board.SCL, board.SDA)
        self.oled = adafruit_ssd1306.SSD1306_I2C(OLED_WIDTH, OLED_HEIGHT, i2c, addr=DISPLAY_I2C_ADDRESS)
        self.multiplexer = multiplexer
        self.channel = channel
        self.bus.write_byte(self.multiplexer, 1 << self.channel)

    def __deselect_all_channels(self):
        for m in MULTIPLEXERS:
            self.bus.write_byte(m, 0x00)

    def __select_channel(self):
        self.__deselect_all_channels()
        self.bus.write_byte(self.multiplexer, 1 << self.channel)

    def write(self, message, size=12, font="DejaVuSans.ttf"):

        self.__select_channel()

        img = Image.new("1", (OLED_WIDTH, OLED_HEIGHT))

        draw = ImageDraw.Draw(img)
        W, H = img.size
        try:
            font = ImageFont.truetype(font, size)
        except OSError:
            font = ImageFont.load_default(size)

        # Get bounding box of the text
        _, _, w, h = draw.textbbox((0, 0), text=message, font=font)

        # Compute center
        x = (W - w) * 0.5
        y = (H - h) * 0.5

        # Draw text
        draw.text((x, y), message, font=font, fill="white")

        self.oled.image(img)
        self.oled.show()

    def show_hieroglyph(self, glyph):
        self.write(glyph, 36, "NotoSansEgyptianHieroglyphs-Regular.ttf")


MULTIPLEXERS = [0x70, 0x71]

DISPLAYS = [
    Display(MULTIPLEXERS[0], 3),
    Display(MULTIPLEXERS[0], 4),
    Display(MULTIPLEXERS[0], 5),
    Display(MULTIPLEXERS[0], 6),
    Display(MULTIPLEXERS[0], 2),
    Display(MULTIPLEXERS[0], 1),
    Display(MULTIPLEXERS[0], 0),
    Display(MULTIPLEXERS[0], 7),
    Display(MULTIPLEXERS[1], 5),
    Display(MULTIPLEXERS[1], 6),
    Display(MULTIPLEXERS[1], 3)
]


def print_debug_info():
    for display in DISPLAYS:
        display.write(f"display no: {DISPLAYS.index(display)}\nmx: {display.multiplexer}\nch: {display.channel}", 10)


def random_hieroglyphs():
    for display in DISPLAYS:
        glyph = random.choice(list(HIEROGLYPHS.values()))
        display.show_hieroglyph(glyph)
