from adafruit_circuitplayground import cp
from neopixels import ControllerLightPatterns
from time import sleep

# the colors are constant and are set to tuples to save memory
RED = (255,0,0)
GREEN = (0, 255,0)
BLUE = (0,0,255)
MAGENTA = (255,0,255)
CYAN = (0,255,255)
YELLOW = (255,255,0)

# the light controller is instantiated with the brightness of 0.1
controller = ControllerLightPatterns(0.1)

# the controller is printed to the console
print(controller)

while True:
    # if the switch is set to True the methods associated with the LightPatterns class are called
    if cp.switch:
        # lights_range is call lighting the neopixels in from position 2 to 7 in red
        controller.light_range(RED, [2,7])
        sleep(1) # the lights stay on for 1 second
        # random lights flash for 0.2 seconds in green
        controller.random_lights(GREEN, 0.2)
        # the lights flash in a mirror pattern in blue
        controller.mirror_lights(BLUE)
        # a snake five neopixels long slithers around the neopixels in yellow
        controller.snake(5, YELLOW, 0.2)
        sleep(1)
    # if the switch is set to False the methods associated with the ControllerLightPatterns class are called
    else:
        # the acceleration values are unpacked into x, y, and z variables
        x,y,z = cp.acceleration
        # when the controller is turned upside down the snake pattern is called in cyan
        controller.idle_state(z, CYAN, 0.2)
        # when the board is tilted to one side the neopixels on that side are lit in green
        controller.half_light(x, GREEN)
        # when the board is tilted to the side the neopixels on that side are lit in magenta
        # with the number of pixels lit increasing as the board is tilted more
        controller.control_feedback(x, MAGENTA)