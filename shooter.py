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
        self.__width = 20
        self.__height = 20
        self.__size = [self.__width, self.__height]
        self.__color = color
        self.__speed = speed
        self.__coordinates = [self.__x, self.__y]

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
        shooter_rect = pg.Rect(self.__coordinates, self.__size)
        pg.draw.rect(display, self.__color, shooter_rect)

    def move_up(self, moveup_trigger):
        """
        This method moves the shooter up.
        The shooter cannot move off the screen.
        
        """
        if moveup_trigger[pg.K_UP]:
            self.__y -= self.__speed
            if self.__y < 0:
                self.__y = 0
            self.__coordinates = [self.__x, self.__y]

    def move_down(self, movedown_trigger):
        """
        This method moves the shooter down.
        The shooter cannot move off the screen.

        """
        if movedown_trigger[pg.K_DOWN]:
            self.__y += self.__speed
            if self.__y > 600 - self.__height: # I don't want to hard code this
                self.__y = 600 - self.__height
            self.__coordinates = [self.__x, self.__y]

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

    def get_coordinates(self):
        """
        This method returns the coordinates of the shooter.

        """
        return self.__coordinates

    def set_coordinates(self, coordinates):
        """
        This method sets the coordinates of the shooter.

        """
        self.__coordinates = coordinates

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
    coordinates = property(get_coordinates, set_coordinates)
    color = property(get_color, set_color)
    speed = property(get_speed, set_speed)
    size = property(get_size, set_size)