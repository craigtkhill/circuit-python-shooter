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

    def smiley_face(self, colors):
        right_mouth = list(range(LightPatterns.num_pixels // 3))
        left_mouth = list(range(LightPatterns.num_pixels - (LightPatterns.num_pixels // 3), LightPatterns.num_pixels))
        mouth = right_mouth + left_mouth
        cheeks = [pixel for pixel in range(LightPatterns.num_pixels) if pixel %3 == 0 and pixel != 0 and pixel != LightPatterns.num_pixels - 1]
        for pixel in range(LightPatterns.num_pixels):
            if pixel in mouth and pixel not in cheeks:
                cp.pixels[pixel] = colors[0]
            elif pixel in cheeks:
                cp.pixels[pixel] = LightPatterns.BLACK 
            else:
                cp.pixels[pixel] = colors[1]
        cp.pixels.show()


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

    def control_feedback(self, acceleration_y, color):
        absolute_y = abs(acceleration_y)
        num_pixels = LightPatterns.num_pixels
        lower_bound = num_pixels // 4
        upper_bound = num_pixels - (num_pixels // 4)
        if absolute_y <= 9.81:
            if acceleration_y > 3:
                scale_range = list(range(lower_bound, upper_bound))
                last_pixel_position = int(absolute_y * 5 / 9.81)
            else: return
            for pixel in scale_range:
                if pixel <= last_pixel_position:
                    cp.pixels[pixel] = color
                    cp.pixels[LightPatterns.num_pixels -1 - pixel] = color
                cp.pixels.show()
        else: self.lights_off()

    def modified_feedback_control(self, acceleration_y, colors):
        if abs(acceleration_y) <= 9.81:
            if acceleration_y < -3:
                self.smiley_face(colors)
                #self.mirror_lights(color[0])
            elif acceleration_y >3:
                self.control_feedback(acceleration_y,colors[2])
            else:
                self.lights_off()

