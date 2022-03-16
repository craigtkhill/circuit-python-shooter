import pygame as pg
from random import randint
class Enemy:
    '''
    Class representing the enemy.

    Attributes
    ----------
        x : int
            the x coordinate of the enemy
        y : int
            the y coordinate of the enemy
        color : tuple or list of RGB values
            the color of the enemy
        size : tuple, list or int
            the height and width of the enemy
        speed_x : int
            the speed of the enemy in the x direction
        speed_y : int
            the speed of the enemy in the y direction
    '''

    def __init__(self, x, y, color, size, speed_x, speed_y):
        '''
        Initializes the Enemy.

        Instance variables are used here to allow multiple enemies to be instantiated 
        with different coordinates, sizes, colors and speeds set individually.
        This allows flexibility if we want to introduce more enemies to make the game
        more challenging.
        '''
        # Coordinates
        self.__x = x
        self.__y = y
        self.__coordinates = [self.__x, self.__y]
        # Color
        self.__color = color
        # if the size parameter is a list or tuple the values are assigned
        # to the size of the enemy, otherwise and new list with two values 
        # is created using a simplied if else statement
        # (https://docs.python.org/3/library/functions.html#isinstance)
        # (https://stackoverflow.com/questions/2802726/putting-a-simple-if-then-else-statement-on-one-line)
        # Size
        self.__size = size if isinstance(size, (list, tuple)) else [size, size]
        # Speed in differnt directions
        self.__speed_x = speed_x
        self.__speed_y = speed_y

    def __str__(self):
        '''
        Returns a string representation of the enemy including it color and location
        '''
        return f'Enemy: {self.__color}. Location: ({self.__x},{self.__y})'

    def draw(self, display):
        '''
        Draws the Enemy on the screen.

        Parameters
        ----------
            display : pygame.display
                the display on which the enemy is drawn
        '''
        # the rectangular coordinates and size are stored in a variable
        # (https://www.pygame.org/docs/ref/rect.html)
        enemy_rect = pg.Rect(self.__coordinates, self.__size)
        # pygame draws the rectangle to the display
        pg.draw.rect(display, self.__color, enemy_rect)

    def move(self, left_bound, right_bound, top_bound, bottom_bound):
        """
        Moves the enemy diagonally while keeping it within the bounds of the screen.

        Parameters
        ----------
            left_bound : int
                the left boundary of the screen
            right_bound : int
                the right boundary of the screen
            top_bound : int
                the top boundary of the screen
            bottom_bound : int
                the bottom boundary of the screen

        """
        # The x and y coordinates are increased by the value of the speed instance variable
        self.__x += self.__speed_x
        self.__y += self.__speed_y
        # if the x coordinate is less than the value of the left bound
        # the speed is reversed by minusing itself
        # and the x coordinate is assigned to the value of the left bound
        if self.__x < left_bound:
            self.__speed_x = -self.__speed_x
            self.__x = left_bound
        # if the x coordinate is greater than the value of the right bound
        # taking into account its width
        # the speed is reversed by minusing itself
        # and the x coordinate is assigned to the value of the the right bound
        if self.__x > right_bound - self.__size[0]:
            self.__speed_x = -self.__speed_x
            self.__x = right_bound - self.__size[0]
        # if the y coordinate is less than the value of the top bound
        # the speed is reversed by minusing itself
        # and the y coordinate is assigned to the value of the left bound
        if self.__y < top_bound:
            self.__speed_y = -self.__speed_y
            self.__y = top_bound
        # if the y coordinate is greater than the value of the bottom bound
        # taking into account its height
        # the speed is reversed by minusing itself
        # and the y coordinate is assigned to the value of the bottom bound
        if self.__y > bottom_bound - self.__size[1]:
            self.__speed_y = -self.__speed_y
            self.__y = bottom_bound - self.__size[1]
        # the enemy's coordinates are updated
        self.__coordinates = [self.__x, self.__y]

    def relocate(self, top_bound, bottom_bound, left_bound, right_bound):
        """
        Reclocates the enemy to a random position within the bounds of the screen

        Parameters
        ----------
            top_bound : int
                the top boundary of the screen
            bottom_bound : int
                the bottom boundary of the screen
            left_bound : int
                the left boundary of the screen
            right_bound : int
                the right boundary of the screen
        """
        # The x and y coordinates are set to a number within the bounds of the screen
        self.__x = randint(left_bound, right_bound)
        self.__y = randint(top_bound, bottom_bound)
        # The enemy's coordinates are updated
        self.__coordinates = [self.__x, self.__y]

    def change_speed(self, lower_limit, upper_limit):
        """
        Changes the speed of the enemy

        Parameters
        ----------
            lower_limit : int
                the lower limit of the speed
            upper_limit : int
                the upper limit of the speed
        """
        # The speed is assigned a random value between the lower and upper limits
        self.__speed_x = randint(lower_limit, upper_limit)
        self.__speed_y = randint(lower_limit, upper_limit)

# Getters for coordinates and size of the enemy below.

    @property
    def coordinates(self):
        '''
        Gets the coordinates of the enemy.

        Returns
        -------
            coordinates : list
                the x and y coordinates of the enemy
        '''
        return self.__coordinates

    @property
    def heigth(self):
        '''
        Gets the height of the enemy.

        Returns
        -------
            size : int
                the height of the enemy
        '''
        return self.__height


    @property
    def width(self):
        '''
        Gets the width of the enemy.

        Returns
        -------
            size : int
                the width of the enemy
        '''
        return self.__width
