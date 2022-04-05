from adafruit_circuitplayground import cp
from neopixels import ControllerLightPatterns
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices) # keyboard device is setup 

acceleration_y = 0 # variable containing the acceleration y value
acceleration_peak = 9.81 # variable containing the maximum acceleration value
bullet_fired = False # boolean holding the state of the bullet

# Colors defined in tuple format
RED = (255,0,0)
GREEN = (0, 255,0)
CYAN = (0,255,255)

colors = [RED,CYAN,GREEN]

controller = ControllerLightPatterns(0.1) # controller light patterns object is initalised with brightness of 10%

print(controller)

while True:
    if cp.switch: # if the cp switch is set to the true position
        x,y,z = cp.acceleration # the acceleration values are stored in x,y,z 
        if abs(y) <= acceleration_peak: # if the absolute value of y is less than the acceleration peak
            if y < -3: # and acceleration y is less than -3
                kbd.press(Keycode.DOWN_ARROW) # the down arrow is pressed
                kbd.release(Keycode.UP_ARROW) # and the up arrow is released
            elif y > 3: # else if the acceleration is greater than 3
                kbd.press(Keycode.UP_ARROW) # the up arrow is pressed
                kbd.release(Keycode.DOWN_ARROW) # and the down arrow is released
            else: # otherwise the board is horizontal and all the keys are released if they are down
                kbd.release_all()
        if cp.button_a: # if the button a is pressed
            if bullet_fired: # and the bullet has already been fired
                bullet_fired = False # the bullet state is set to false
            else: # if the bullet has not been fired
                kbd.press(Keycode.SPACEBAR) # then the spacebar is pressed, firing the bullet
                bullet_fired = True # and the bullet is set to the true state
        # the controller modified feedback method provides feedback using neopixels to display the
        # direction the board is tilting, it takes the y acceleration values and a list of colors
        controller.modified_feedback_control(y, colors)
    else: # if the cp switch is set to false
        controller.lights_off() # the neopixels are turned off
        kbd.release_all() # and the keys are released

