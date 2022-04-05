from adafruit_circuitplayground import cp

class LightPatterns:
    # class variables are used as they save memory and will not change between instances
    BLACK = (0, 0, 0) # variable to turn neopixels off by changing the color to black
    cp.pixels.auto_write = False # neopixels will only update with show method is called
    num_pixels = len(cp.pixels) # number of neopixels is equal to the length of cp.pixels

    def __init__(self, brightness):
        cp.pixels.brightness = brightness # the brightness of the neopixels is set to the brightness of the light patterns object

    def __str__(self): # string representation of the LightPatterns class with number of neopixels and brightness
        return f'Pixels {LightPatterns.num_pixels}, Brightness {cp.pixels.brightness}'

    def lights_off(self): # turns neopixels off
        cp.pixels.fill(LightPatterns.BLACK) # the neopixels are set to black
        cp.pixels.show() # and the neopixels are updated

    def smiley_face(self, colors): # lights up the board with a smiley face
        # the mouth is created by creating lists of the neopixels from 0 to a third of the board
        # the last third of the board to the end
        # and joining the lists together
        right_mouth = list(range(LightPatterns.num_pixels // 3))
        left_mouth = list(range(LightPatterns.num_pixels - (LightPatterns.num_pixels // 3), LightPatterns.num_pixels))
        mouth = right_mouth + left_mouth
        # the eyes are the two neopixels halfway on the board
        eyes = [(LightPatterns.num_pixels // 2) , (LightPatterns.num_pixels // 2) -1]
        for pixel in range(LightPatterns.num_pixels): # for each pixel on the board
            if pixel in mouth: # if the neopixels are in the position of the mouth
                cp.pixels[pixel] = colors[0] # they are colored (red)
            elif pixel in eyes: # if the neopixels are in the positon of the eyes
                cp.pixels[pixel] = colors[1] # they are colored (cyan)
            else: # otherwise the neopixels are colored black
                cp.pixels[pixel] = LightPatterns.BLACK
        cp.pixels.show() # and the neopixels are updated


class ControllerLightPatterns(LightPatterns): # class providing feedback degree of tilt using neopixels
    # inherits init, str and other methods from the LightPatterns class

    def control_feedback(self, acceleration_y, color): 
        # lights up the the top of the board in a mirror pattern with more pixels the greater the tilt
        absolute_y = abs(acceleration_y) # the absolute value of acceleration y is stored in a variable
        # the number of pixels is stored in a variable using the light patterns class variable 
        # this shortened version of num_pixels is used make the code more readable
        num_pixels = LightPatterns.num_pixels
        lower_bound = num_pixels // 4 # the lower bound of the neopixels is a quarter the number of neopixels (neopixel 3)
        upper_bound = num_pixels - (num_pixels // 4) # the upper bound is the number of pixels minus a quarter (9 - 3 = neopixel 6)
        if absolute_y <= 9.81: # if the absolute y is less than or equal to 9.81
            if acceleration_y > 3: # and acceleration y is greater than 3
            # a list of neopixels is created from the lowerbound to the upperbound (3 -> 6)
                neopixels = list(range(lower_bound, upper_bound)) 
                # the last pixels position is the acceleration values times half the number of pixels 
                # scaled to the highest possible acceleration values
                last_pixel_position = int(absolute_y * (num_pixels // 2) / 9.81)
            else: return # if the acceleration values is less than three, the method is exited without doing anything
            for pixel in neopixels: # for each pixel in the range of neopixels to be filled
                if pixel <= last_pixel_position: # if the pixel number is less than or equal to the last pixel position
                    cp.pixels[pixel] = color # the pixel is colored
                    cp.pixels[LightPatterns.num_pixels -1 - pixel] = color # and the pixel on the mirroring side of the board is also colored 
                cp.pixels.show() # the pixels are then updated
        else: self.lights_off() # if the acceleration value is not between -9.81 and 9.81, the lights are turned off

    def modified_feedback_control(self, acceleration_y, colors): 
        # updates the lights patterns depending on the direction the board is tilted
        if abs(acceleration_y) <= 9.81: # if the absolute y value is less than or equal to 9.81
            if acceleration_y < -3: # and acceleration y is less than -3
                self.smiley_face(colors) # the smiley_face method is called from the LightPatterns class
            elif acceleration_y > 3: # if the acceleration y is greater than 3
                self.control_feedback(acceleration_y, colors[2]) # the control_feedback method is called
            else: # if the acceleration y value is between -3 and 3 then the lights are turned off
                self.lights_off()

