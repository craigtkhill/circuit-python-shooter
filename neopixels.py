from adafruit_circuitplayground import cp
from time import sleep
from random import randint

class LightPatterns:
    BLACK = (0, 0, 0)
    cp.pixels.auto_write = False
    num_pixels = len(cp.pixels)

    def __init__(self, brightness):
        cp.pixels.brightness = brightness

    def __str__(self):
        return f'Pixels {LightPatterns.num_pixels}, Brightness {cp.pixels.brightness}'

    def lights_off(self):
        cp.pixels.fill(LightPatterns.BLACK)
        cp.pixels.show()

    def light_range(self, color, ran):
        self.lights_off()
        if len(ran) != 2: return
        if min(ran) < 0: return
        if max(ran) > LightPatterns.num_pixels: return
        else:
            for pixel in range(ran[0], ran[1] + 1):
                cp.pixels[pixel] = color
        cp.pixels.show()

    def random_lights(self, color, interval):
        self.lights_off()
        random_list = []
        while len(random_list) < 5:
            random_num = randint(0, LightPatterns.num_pixels - 1)
            if random_num not in random_list:
                random_list.append(random_num)
        for _ in range(5):
            for pixel in random_list:
                cp.pixels[pixel] = color
            cp.pixels.show()
            sleep(interval)
            self.lights_off()
            sleep(interval)

    def mirror_lights(self, color):
        for pixel in range(LightPatterns.num_pixels // 2):
            cp.pixels[pixel] = color
            cp.pixels[LightPatterns.num_pixels -1 - pixel] = color
            cp.pixels.show()
            sleep(0.2)
        self.lights_off()

    def snake(self, snake_size, color, interval):
        self.lights_off()
        if snake_size < 2 or snake_size > (LightPatterns.num_pixels // 2): return
        snake = list(range(snake_size))
        while len(snake) >1:
            for pixel in snake:
                if snake[-1] > LightPatterns.num_pixels - 1:
                    snake.pop()
                cp.pixels[pixel] = color
            cp.pixels.show()
            sleep(interval)
            snake.append(snake[-1] +1)
            snake.pop(0)
            self.lights_off()

class ControllerLightPatterns(LightPatterns):

    def idle_state(self, acceleration_z, color, interval):
        if acceleration_z <= -7 and acceleration_z >= -9.81:
            self.snake(5, color, interval)
        else: self.lights_off()

    def half_light(self, acceleration_x, color):
        if abs(acceleration_x) <= 9.81:
            if acceleration_x > 3:
                for pixel in range(LightPatterns.num_pixels // 2):
                    cp.pixels[pixel] = color
                cp.pixels.show()
            elif acceleration_x < -3:
                for pixel in range(LightPatterns.num_pixels // 2, LightPatterns.num_pixels):
                    cp.pixels[pixel] = color
                cp.pixels.show()
            else: self.lights_off()

    def control_feedback(self, acceleration_x, color):
        absolute_x = abs(acceleration_x)
        if absolute_x <= 9.81:
            if 2 <= acceleration_x <= 9.81:
                scale_range = list(range(LightPatterns.num_pixels // 2))
                last_pixel_position = int(absolute_x * 5 / 9.81)
            elif -2 >= acceleration_x >= -9.81:
                scale_range = list(range(LightPatterns.num_pixels // 2, LightPatterns.num_pixels))
                last_pixel_position = int(absolute_x * LightPatterns.num_pixels / 9.81)
            else: return
            last_pixel_position = int(absolute_x * LightPatterns.num_pixels / 9.81)
            if last_pixel_position != 0:
                for pixel in scale_range:
                    if pixel <= last_pixel_position:
                        cp.pixels[pixel] = color
                    cp.pixels.show()
        else: self.lights_off()
