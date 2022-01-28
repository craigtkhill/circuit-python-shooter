import pygame as pg
class Shooter:
    '''
    Class representing the Shooter.

    '''
    # need to defend my choice of instance variables versus class variables
    def __init__(self, x, y, color, speed):
        '''
        Constructor for the Shooter class.

        '''
        self.__x = x
        self.__y = y
        self.__width = 10
        self.__height = 10
        self.__color = color
        self.__speed = speed
        self.coordinates = [self.__x, self.__y]

    def __str__(self):
        '''
        Returns a string representation of the Shooter including its color and coordinates.

        '''
        return f'Shooter: {self.__color}. Location: ({self.__x},{self.__y})'

    def draw(self, display):
        '''
        Draws the Shooter on the screen.

        '''
        # can make this into another shape later if I want
        pg.draw.rect(display, self.__color, (self.__x, self.__y, self.__width, self.__height))

    def move_up(self, moveup_trigger):
        """
        This method moves the shooter up.
        The shooter cannot move off the screen.
        
        """
        pass

    def move_down(self, movedown_trigger):
        """
        This method moves the shooter down.
        The shooter cannot move off the screen.

        """
        pass

    def get_x(self):
        """
        This method returns the x coordinate of the shooter.

        """
        return self.__x

    def set_x(self, x):
        """
        This method sets the x coordinate of the shooter.

        """
        self._x = x

    def get_y(self):
        """
        This method returns the y coordinate of the shooter.

        """
        return self.__y

    def set_y(self, y):
        """
        This method sets the y coordinate of the shooter.

        """
        self.__y = y

    def get_color(self):
        """
        This method returns the color of the shooter.

        """
        return self.__color

    def set_color(self, color):
        """
        This method sets the color of the shooter.

        """
        self.__color = color

    def get_speed(self):
        """
        This method returns the speed of the shooter.

        """
        return self.__speed

    def set_speed(self, speed):
        """
        This method sets the speed of the shooter.

        """
        self.__speed = speed

    def get_size(self):
        """
        This method returns the size of the shooter.

        """
        return self.__width, self.__height

    def set_size(self, width, height):
        """
        This method sets the size of the shooter.

        """
        self.__width = width
        self.__height = height

    x = property(get_x, set_x)
    y = property(get_y, set_y)
    color = property(get_color, set_color)
    speed = property(get_speed, set_speed)
    size = property(get_size, set_size)