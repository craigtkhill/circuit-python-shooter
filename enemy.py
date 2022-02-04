import pygame as pg
class Enemy:
    '''
    Class representing the enemy.

    Attributes
    ----------
        x : int
            the x coordinate of the enemy
        y : int
            the y coordinate of the enemy
        color : tuple or list
            the color of the enemy
        size : tuple, list or int
            the size of the enemy
        speed_x : int
            the speed of the enemy in the x direction
        speed_y : int
            the speed of the enemy in the y direction
    '''

    def __init__(self, x, y, color, size, speed_x, speed_y):
        '''
        Initializes the Enemy.

        Parameters
        ----------
            x : int
                the x coordinate of the enemy
            y : int
                the y coordinate of the enemy
            color : tuple or list
                the color of the enemy
            size : tuple, list or int
                the size of the enemy
            speed_x : int
                the speed of the enemy in the x direction
            speed_y : int
                the speed of the enemy in the y direction
        '''
        # Instance Variable - Multiple enemys can be instantiated with different coordinates
        # allows flexiblity if we want intoduce more enemies
        self.__x = x
        self.__y = y
        self.__coordinates = [self.__x, self.__y]
        # Instance Variables - The colors, sizes and speeds for each enemy can be set individually
        self.__color = color
        # if the size parameter is a list the values in the list are assigned
        # to the size of the enemy, otherwise and new list with two values 
        # is created using a simplied if else statement
        # (https://docs.python.org/3/library/functions.html#isinstance)
        # (https://stackoverflow.com/questions/2802726/putting-a-simple-if-then-else-statement-on-one-line)
        self.__size = size if isinstance(size, list) else [size, size]
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
            display : pygame.Surface
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
        self.__coordinates = [self.__x, self.__y]

    @property
    def coordinates(self):
        '''
        Gets the coordinates of the enemy.

        Returns
        -------
            coordinates : list
                the coordinates of the enemy
        '''
        return self.__coordinates

    @coordinates.setter
    def coordinates(self, x=None, y=None):
        '''
        Sets the coordinates of the enemy.

        Parameters
        ----------
            x : int
                the x coordinate of the enemy
            y : int
                the y coordinate of the enemy
        '''
        if x is not None:
            self.__x = x
        if y is not None:
            self.__y = y

        self.__coordinates = [self.__x, self.__y]

    @property
    def size(self):
        '''
        Gets the size of the enemy.

        Returns
        -------
            size : list
                the size of the enemy
        '''
        return self.__size

    @size.setter
    def size(self, width=None, height=None):
        """
        Sets the size of the enemy.

        Parameters
        ----------
            width : int
                the width of the enemy
            height : int
                the height of the enemy
        """
        if width is not None:
            width = self.__width
        if height is not None:
            height = self.__height
            
        self.__size = [self.__width, self.__height]  
