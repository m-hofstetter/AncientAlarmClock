import threading
from time import sleep

import board, neopixel, time, math, colorsys

PIXEL_PIN = board.D16
NUM_PIXELS = 56

class Neopixels:
    def __init__(self):
        self.pixels = neopixel.NeoPixel(PIXEL_PIN, NUM_PIXELS, brightness=1, auto_write=False)
        self.__running = False
        self.__thread = None

    def __scaled_sin(self, x, average, amplitude, period):
        return average + amplitude/2 * math.sin(x * 1/period)

    def __scaled_sin_of_time(self, x, average, amplitude, period):
        t = time.time_ns() / 100_000_000
        return  self.__scaled_sin(t + x, average, amplitude, period)

    def __green_oscillate_per_pixel(self, pixel_number):

        global_hue_factor = self.__scaled_sin_of_time(0, 1, 1, 5)
        hue = self.__scaled_sin_of_time(pixel_number, 0.36, 0.05, 11) * global_hue_factor

        saturation = self.__scaled_sin_of_time(pixel_number, 0.95, 0.1, 3)

        global_brightness_factor = self.__scaled_sin_of_time(0, 0.9, 0.2, 2) + self.__scaled_sin_of_time(0, 0.8, 0.4, 5)
        brightness_a = self.__scaled_sin_of_time(pixel_number, 0.6, 0.8, 3)
        brightness_b = self.__scaled_sin_of_time(-pixel_number, 0.6, 0.8, 5)
        brightness = global_brightness_factor * brightness_a * brightness_b

        r, g, b = colorsys.hsv_to_rgb(hue % 1.0, max(0, min(1, saturation)), max(0, min(1, brightness)))
        return int(r * 255), int(g * 255), int(b * 255)

    def green_oscillate_update_all_pixels(self):
        for i in range(NUM_PIXELS):
            self.pixels[i] = self.__green_oscillate_per_pixel(i)
        self.pixels.show()

    def __ambient_light_thread(self):
        while self.__running:
            self.green_oscillate_update_all_pixels()
            sleep(0.01)

    def start(self):
        self.__running = True
        self.__thread = threading.Thread(target=self.__ambient_light_thread)
        self.__thread.start()

    def stop(self):
        self.__running = False
        if self.__thread is not None:
            self.__thread.join()
        self.pixels.fill((0, 0, 0))
        self.pixels.show()