from PIL import Image, ImageFont, ImageDraw

OLED_WIDTH = 128
OLED_HEIGHT = 64

CLEAR = Image.new("1", (OLED_WIDTH, OLED_HEIGHT))


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


def generate_image(text, font):
    img = Image.new("1", (OLED_WIDTH, OLED_HEIGHT))
    draw = ImageDraw.Draw(img)
    draw.text((OLED_WIDTH/2, OLED_HEIGHT/2), text, font=font, fill="white", anchor="mm")
    return img


class ImageGenerator:
    def __init__(self, font="DejaVuSans.ttf", size=12):
        try:
            self.latin_font = ImageFont.truetype(font, size)
        except OSError:
            self.latin_font = ImageFont.load_default(size)
        try:
            self.glyph_font = ImageFont.truetype("NotoSansEgyptianHieroglyphs-Regular.ttf", 36)
        except OSError:
            self.glyph_font = ImageFont.load_default(size)

    def generate_text_image(self, text):
        return generate_image(text, self.latin_font)

    def generate_hieroglyph(self, glyph):
        return generate_image(HIEROGLYPHS[glyph], self.glyph_font)