from adafruit_circuitplayground import cp
from neopixels import ControllerLightPatterns
from time import sleep
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)

acceleration_y = 0
acceleration_peak = 9.81
bullet_fired = False

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
        x,y,z = cp.acceleration
        if abs(y) <= acceleration_peak:
            if y < -3:
                kbd.press(Keycode.DOWN_ARROW)
                kbd.release(Keycode.UP_ARROW)
            elif y > 3:
                kbd.press(Keycode.UP_ARROW)
                kbd.release(Keycode.DOWN_ARROW)
            else:
                kbd.release_all()
        if cp.button_a:
            if not bullet_fired:
                kbd.send(Keycode.SPACEBAR)
                bullet_fired = True
            else:
                bullet_fired = False
        controller.modified_feedback_control(y, [RED,YELLOW, GREEN])

