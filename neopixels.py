# import the circuit board express library

class LightPatterns:
    """
    This class contains generic Neopixel light patterns
    """
    # the color black is set as a class variable as this will not change between instances
    __BLACK = (0, 0, 0)

    def __init__(self, brightness):
        """
        Initializes the LightPatterns class
        """
        # justification for instance variable
        self.__num_pixels = 0 ## should not be hardcoded, should reference the board
        self.__brightness = brightness
        ## Setting up the neopixel environment so that the neopixels only update when requested.

    def __str__(self):
        """
        A string representation of the LightPatterns class
        """
        return f'LightPatterns: Pixels {self.__num_pixels}, Brightness {self.__brightness}'

    def lights_off(self):
        """
        Turns all the neopixels off
        """
        # the neopixels are set to black
        self.__pixels = [self.__BLACK] * self.__num_pixels

    def light_range(self, color, ran):
        """
        
        This method accepts the following parameters: 
        colour (list): the colour to light the neopixels 
        ran (list): a two-value integer list representing the range of neopixels to light up 
 
        This method should light up the neopixels from a specified range (defined in ran, inclusive of 
        both values in the list) with a specified colour (defined in colour). All other neopixels should be 
        switched off. Note the following: 
            • You may assume that ran is a list, and that it contains integer numbers 
            • The ran list must be of length 2 – and you must check for this before lighting up the neopixels. 
            • You may assume the integers inside ran are sorted from lowest to highest 
            • The two values inside the list can be the same value 
            • The lowest value inside ran must not be less than 0. The highest value inside ran must not be higher than the value of the last pixel position. 
            • You may assume that colour is a list, and contains only three integer values, each integer between 0 and 255 (inclusive of both). """
        pass

    def random_lights(self, color, interval):
        """       
        This method accepts the following as arguments: 
            • colour (list): the colour of the neopixels 
            • interval (float): the time in seconds between each neopixel on state  
 
        This method should light neopixels at five unique random locations at the same time. These random locations should flash five times. Note the following  
            • The light should be coloured using the colour value passed in to the method.  
            • You may assume that colour is a list, and contains only three integer values, each integer between 0 and 255 (inclusive of both). 
            • The light should remain on for the period of time specified in interval 
            • The light should then switch off for the period of time specified in interval 
            Note: you must use a loop in this method."""
        pass

    def mirror_lights(self, color):
        """
        This method accepts the following as arguments: 
            • colour (list): the colour of the lights  
 
        This method should light up the neopixels in the following pattern, with a time interval of your  choice in between the new neopixels lighting up: 
            • position 0 and last_neopixel at the same time 
            • position 1 and last_neopixel – 1 at the same time 
            • position 2 and last_neopixel – 2 at the same time 
            • position 3 and last_neopixel – 3 at the same time 
            • position 4 and last_neopixel – 4 at the same time 
        Once all neopixels have been lighted, all neopixels should switch off. 
        Note: you must use a loop in this method. You may assume that colour is a list, and contains only three integer values, each integer between 0 and 255 (inclusive of both).
        """
        pass
    
    def snake(self, snake_size, color, interval):
        """This method accepts the following as arguments: 
                • snake_size (int): the size of the snake, i.e. the number of consecutive neopixels to light 
                • colour (list): the colour of the neopixels 
                • interval (float): the time in seconds between each neopixel on state
            
            Using a loop to give the illusion of movement of a snake, this method should: 
                • initially light up neopixels from position 0 to neopixels at position 0 + snake_size. All 
                other neopixels should be switched off.  
                • All lighted neopixels from the next position upwards should light up (from position 1 to 
                position 1 + snake_size). 
                • This pattern should continue until the last neopixel lighted is the last neopixel available. 
 
            Note the following: 
                • snake_size should not be less than 2 or greater than half the amount of neopixels on the board. If it is, the method should terminate."""
        pass

class ControllerLightPatterns(LightPatterns):
    """
    This class controls the Neopixel light patterns in response to the sensor input
 
    Note it is possible to inherit LightPatterns and to reuse parent methods in all methods inside ControllerLightPatterns. Applying inheritance correctly and efficiently, with code fully working, will place the student’s work for this question higher in the grading band (see grading criteria).

    The ControllerLightPatterns class contains the following variables. You may decide 
        whether the variables below are class or instance variables. However, you will need to defend your choice in your comments. 
            (i) Variable to hold the colour black 
            (ii) Variable for holding the amount of neopixels on the board. This value should reference the board’s neopixels and should not be hardcoded.
    """
    pass

    def __init__(self, brightness):
        """
        Note that it is possible to use inheritance here.  
        The constructor should be used to set up the ControllerLightPatterns class. This includes: 
        - Setting up the brightness of the neopixels, which is defined by the parameter called 
        brightness 
        - Setting up the neopixel environment so that the neopixels only update when requested.
        """
        pass
    def idle_state(self, acceleration_z, color, interval):
        """
        This method accepts the following arguments: 
            • acceleration_z: the z acceleration value 
            • colour: the colour to light the neopixels when lighted 
            • interval: the amount of time between each light 
        
        This method determines if the board is in idle state, which is triggered when the board is upside down. 
        
        To do so, it should check if the acceleration_z  value is between -7 and -9.81 (inclusive of both). 
            • If it is, then this method should call the snake() method from the LightPatterns class. 
        You can pass in a hard coded value for the snake size in this case. 
            • If it is not, all neopixels should be switched off. Note that the snake lights may not switch off instantly – the entire cycle may need to be completed first.
        """
        pass

    def half_light(self, acceleration_x, color):
        """ 
        This method accepts the following arguments: 
            • acceleration_x: the x acceleration value 
            • colour: the colour to light the neopixels when lighted 
        
        This method should:
            • Check if the acceleration x value is less than 9.81 or greater than -9.81. ONLY if this is the case: 
                - light up neopixels at positions 5 - 9 inclusive if the acceleration_x value is less than -3 on the x axis 
                - light up neopixels at positions 0 - 4 inclusive if the acceleration_x value is greater than 3 on the x axis 
                - Otherwise, the neopixels should all switch off. 
            Note: you must use loops in this method. 
        """
        pass

    def control_feedback(self, acceleration_x, color):
        """  
        This method accepts the following arguments: 
            • acceleration_x (float): the x acceleration of the board 
            • colour (list): the colour to light the neopixels. 
        
        This method does the following: 
            - Checks if the acceleration_x is within the range of -9.81 and +9.81, inclusive of both. 
            • If this is not the case, then the rest of the code in the method should not execute. 
            - If the acceleration_x is within the range, then: 
            • Map the acceleration_x value to the range of neopixels that should be lighted using the following guidance: 
            • If the acceleration_x value is greater than 2, then the acceleration_x value 
        should be scaled from between: 
                    o 0 ----------------- 9.81 
                            to the integer range of: 
                    o 0 ------------------ 4 
            •  If the acceleration_x value is less than -2, then the acceleration value should be scaled from between: 
                    o 0 ----------------- –9.81 
                            to the integer range of: 
                    o 5 ------------------ 9 
            • All neopixels in the ranges specified above should be lighted with the value inside colour 
            • For example, let's say the x acceleration value was 4: This value is greater than 2. When mapped to the integer range of (0 ----> 4), the pixel range value would be roughly 2. This means we should light neopixels from 0 up until and including, 2. All other neopixels should be switched off. 
            • Another example, let’s say the x acceleration value was -4. This value is less than -2. When mapped to the integer range of (5 ----> 9), the pixel range value would be roughly 7. This means we should light neopixels from 5 up until and including 7. All other neopixels should be switched off."""
            pass