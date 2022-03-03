from adafruit_circuitplayground import cp
from neopixels import ControllerLightPatterns
from time import sleep

RED = (255,0,0)
GREEN = (0, 255,0)
BLUE = (0,0,255)
MAGENTA = (255,0,255)
CYAN = (0,255,255)
YELLOW = (255,255,0)

controller = ControllerLightPatterns(0.1)

print(controller)

while True:
    if cp.switch:
        controller.light_range(RED, [2,7])
        sleep(1)
        controller.random_lights(GREEN, 0.2)
        controller.mirror_lights(BLUE)
        controller.snake(5, YELLOW, 0.2)
        sleep(1)
    else:
        x,y,z = cp.acceleration
        controller.idle_state(z, CYAN, 0.2)
        controller.half_light(x, GREEN)
        controller.control_feedback(x, MAGENTA)
