from adafruit_circuitplayground import cp
from time import sleep
from random import randint

class LightPatterns:
    """This class contains generic Neopixel light patterns"""
    # the color black, auto_write and number of pixels are set as class variables 
    # as these will not change between instances 
    # and saves memory compared to the use of instance variables
    BLACK = (0, 0, 0)
    cp.pixels.auto_write = False
    num_pixels = len(cp.pixels)

    def __init__(self, brightness):
        """Initializes the LightPatterns class"""
        # the brightness can change between instances
        cp.pixels.brightness = brightness

    def __str__(self):
        """A string representation of the LightPatterns class"""
        return f'Pixels {LightPatterns.num_pixels}, Brightness {cp.pixels.brightness}'

    def lights_off(self):
        """Turns all the neopixels off - The neopixels colors are set to black"""
        # the neopixels are turned off by setting the color to black
        cp.pixels.fill(LightPatterns.BLACK)
        # the neopixels are then updated
        cp.pixels.show()

    def light_range(self, color, ran):
        """
        Lights up the neopixels in a specified color and range
        
        Parameters 
        ----------
            color : list or tuple 
                the color for the neopixel light
            ran : list
                two value integer list representing the range of neopixels to be lit
        """
        # the neopixels are turned off
        self.lights_off()
        # the ran parameter is checked to make sure it is 
        # a list of two integers
        # the minimum value of the range is 0
        # the maximum value of the range is the number of neopixels
        # if any of the conditions are met the method returns without doing anything
        if len(ran) != 2: return
        if min(ran) < 0: return
        if max(ran) < LightPatterns.num_pixels: return
        # otherwise the neopixels are lit up in the specified range
        else:
            for pixel in range(ran[0], ran[1] + 1): # +1 as range() is exclusive of last value
                # for each neopixel, the color is set
                cp.pixels[pixel] = color
        # the neopixels are then updated
        cp.pixels.show()

    def random_lights(self, color, interval):
        """
        Lights the neopixels at 5 unique random locations 5 times
        
        Parameters 
        ----------
            color : list or tuple
                the color for the neopixel light
            interval : float
                time in seconds between each neopixel on state
        """
        # the neopixels are turned off
        self.lights_off()
        # a empty list to store the random locations is initialized
        random_list = []
        # while the length of the random list is less than 5
        # the randint method is called to generate a random number
        # if the random number is not in the random list
        # the random number is added to the random list
        while len(random_list) < 5:
            random_num = randint(0, LightPatterns.num_pixels - 1)
            if random_num not in random_list:
                random_list.append(random_num)
        # the neopixels are then lit up at the random locations and updated
        for _ in range(5):
            for pixel in random_list:
                cp.pixels[pixel] = color
            cp.pixels.show()
        # the neopixels staty lit for the specified interval
            sleep(interval)
        # the neopixels are then turned off for the same specified interval
            self.lights_off()
            sleep(interval)

    def mirror_lights(self, color):
        """
        Lights the neopixels in a mirror pattern
        
        Parameters 
        ----------
            color : list or tuple
                the color for the neopixel light
        """
        # for each neopixel in the range of zero to half the number of neopixels
        for pixel in range(LightPatterns.num_pixels // 2):
            # the neopixels are lit up in the specified color
            cp.pixels[pixel] = color
            # and the inverse neopixels are lit up in the specified color
            cp.pixels[LightPatterns.num_pixels -1 - pixel] = color
            cp.pixels.show()
            # neopixels are lit for 0.2 seconds
            sleep(0.2)
        # when all the neopixels have been lit up, the neopixels are turned off
        self.lights_off()

    def snake(self, snake_size, color, interval):
        """
        Lights the neopixels in a snake pattern

        Parameters 
        ----------
            snake_size : int
                the length of the snake in number of neopixels
            color : list or tuple
                the color for the neopixel light
            interval : float
                time in seconds between each neopixel on state
        """
        # the neopixels are turned off
        self.lights_off()
        # if the length of the snake is less than 2 or greater than half the number of neopixels
        # the method returns without doing anything
        if snake_size < 2 or snake_size > (LightPatterns.num_pixels // 2): return
        # a list of values holding the snake's position is initialized
        snake = list(range(snake_size))
        # while the length of the snake is greater than 1
        while len(snake) >1:
            # for each neopixel in the snake
            for pixel in snake:
                # if the head of the snake is greater than the number of neopixels
                # the last value of the snake is removed using the pop method
                # https://docs.python.org/3/tutorial/datastructures.html <- pop method
                if snake[-1] > LightPatterns.num_pixels - 1:
                    snake.pop()
                # otherwise the neopixel is lit up in the specified color and updated
                cp.pixels[pixel] = color
            cp.pixels.show()
            # the neopixels are lit for the specified interval
            sleep(interval)
            # then the value of the head of the snake is appended
            snake.append(snake[-1] +1)
            # and the tail of the snake is removed
            snake.pop(0)
            self.lights_off()
            # once the length of the snake is 1, the while loop is exited

class ControllerLightPatterns(LightPatterns):
    """This class contains the code that responds to the accelerometer"""

    # __init__ & __str__ is inherited from the LightPatterns class

    def idle_state(self, acceleration_z, color, interval):
        """
        Lights the neopixels with a snake pattern when the board is upside down
        
        Parameters 
        ----------
            acceleration_z : float
                the z acceleration value
            color : list or tuple
                the color for the neopixel light
            interval : float
                time in seconds between each neopixel on state
        """
        # if the z acceleration is between -7 and -9.81
        # the snake method is called
        if acceleration_z <= -7 and acceleration_z >= -9.81:
            self.snake(5, color, interval)
        # Otherwise, the neopixels are then turned off
        else: self.lights_off()

    def half_light(self, acceleration_x, color):
        """
        Lights the neopixels on the side the board is tilted to.
        
        Parameters 
        ----------
            acceleration_x : float
                the x acceleration value
            color : list or tuple
                the color for the neopixel light
        """
        # if the absolute value of the x acceleration is less than or equal to 9.81
        # the code below is executed
        # https://docs.python.org/3/library/functions.html#abs <- abs() function
        if abs(acceleration_x) <= 9.81:
            # if the x acceleration is greater than 3
            # the neopixels from 0 to half the number of pixels are lit up in the specified color
            if acceleration_x > 3:
                for pixel in range(LightPatterns.num_pixels // 2):
                    cp.pixels[pixel] = color
                cp.pixels.show()
            # if the x acceleration is less than -3
            # the neopixels from 0 half the number of pixels to the end are lit up in the specified color
            elif acceleration_x < -3:
                for pixel in range(LightPatterns.num_pixels // 2, LightPatterns.num_pixels):
                    cp.pixels[pixel] = color
                cp.pixels.show()
            # otherwise, the neopixels are turned off
            else: self.lights_off()

    def control_feedback(self, acceleration_x, color):
        """
        Lights the neopixels on the side the board is tilted towards with an 
        increasing number of neopixels lit the steeper the angle of tilt.
        
        Parameters 
        ----------
            acceleration_x : float
                the x acceleration value
            color : list or tuple
                the color for the neopixel light
        """
        # if the absolute value of the x acceleration is less than or equal to 9.81
        # the code below is executed
        absolute_x = abs(acceleration_x)
        if absolute_x <= 9.81:
            # if the x acceleration is greater than 2 and less than 9.81
            # a list of values from 0 to half the number of pixels is initialized
            if 2 <= acceleration_x <= 9.81:
                scale_range = list(range(LightPatterns.num_pixels // 2))
            # if the x acceleration is less than -2 and greater than -9.81
            # a list of values from half the number of pixels to the end is initialized
            elif -2 >= acceleration_x >= -9.81:
                scale_range = list(range(LightPatterns.num_pixels // 2, LightPatterns.num_pixels))
            # otherwise, the method returns without doing anything
            else: return
            # the x acceleration is mapped to the neopixels by using
            # the absolute x acceleration value times the number of pixels divided by acceleration peak
            last_pixel_position = int(absolute_x * LightPatterns.num_pixels / 9.81)
            # if the end pixel position is greater than zero the code below is executed
            if last_pixel_position > 0:
                # for each neopixel in its scaled range, the neopixel is lit up in the specified color
                for pixel in scale_range:
                    if pixel <= last_pixel_position:
                        cp.pixels[pixel] = color
                    cp.pixels.show()
        # otherwise, the neopixels are turned off
        else: self.lights_off()
