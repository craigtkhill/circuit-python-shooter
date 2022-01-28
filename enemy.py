import pygame as pg
class Enemy:
    '''
    Class representing the Enemy.

    '''
    # need to defend my choice of instance variables versus class variables

    def __init__(self, x, y, color, size, speed_x, speed_y):
        '''
        Constructor for the Enemy class.

        size can be passed in as a list or a single value
        '''
        self.__x = x
        self.__y = y
        # commit on this later
        self.__size = size if isinstance(size, list) else [size, size]
        self.__color = color
        self.__speed_x = speed_x
        self.__speed_y = speed_y
        self.coordinates = [self.__x, self.__y]

    def __str__(self):
        '''
        Returns a string representation of the Enemy.

        '''
        return f'Enemy: {self.__color}. Location: ({self.__x},{self.__y})'

    def draw(self, display):
        '''
        Draws the Enemy on the screen.

        '''
        # can make this into another shape later if I want
        pg.draw.rect(display, self.__color, (self.__x, self.__y, self.__size))

    def move(self, left_bound, right_bound, top_bound, bottom_bound):
        """
        This method moves the enemy diagonally.

        Speed defined in an instance variable
        The enemy cannot move off the screen.
        The enemy should change direction when it reaches the edge of the screen.
        Take into account the size of the enemy.

        """
        pass

    def get_x(self):
        '''
        Returns the x coordinate of the Enemy.

        '''
        return self.__x

    def set_x(self, x):
        '''
        Sets the x coordinate of the Enemy.

        '''
        self.__x = x

    def get_y(self):
        '''
        Returns the y coordinate of the Enemy.

        '''
        return self.__y

    def set_y(self, y):
        '''
        Sets the y coordinate of the Enemy.

        '''
        self.__y = y

    def get_size(self):
        '''
        Returns the size of the Enemy.

        '''
        return self.__size

    def set_size(self, size):
        '''
        Sets the size of the Enemy.

        '''
        self.__size = size if isinstance(size, list) else [size, size]

    def get_color(self):
        '''
        Returns the color of the Enemy.

        '''
        return self.__color

    def set_color(self, color):
        '''
        Sets the color of the Enemy.

        '''
        self.__color = color

    def get_speed_x(self):
        '''
        Returns the speed of the Enemy in the x direction.

        '''
        return self.__speed_x

    def set_speed_x(self, speed_x):
        '''
        Sets the speed of the Enemy in the x direction.

        '''
        self.__speed_x = speed_x

    def get_speed_y(self):
        '''
        Returns the speed of the Enemy in the y direction.

        '''
        return self.__speed_y

    def set_speed_y(self, speed_y):
        '''
        Sets the speed of the Enemy in the y direction.

        '''
        self.__speed_y = speed_y

    x = property(get_x, set_x)
    y = property(get_y, set_y)
    size = property(get_size, set_size)
    color = property(get_color, set_color)
    speed_x = property(get_speed_x, set_speed_x)
    speed_y = property(get_speed_y, set_speed_y)   
