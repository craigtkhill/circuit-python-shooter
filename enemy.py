import pygame as pg
class Enemy:
    '''
    Class representing the Enemy.

    '''

    def __init__(self, x, y, color, size, speed_x, speed_y):
        '''
        Constructor for the Enemy class.

        size can be passed in as a list or a single value
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
        Returns a string representation of the Enemy.

        '''
        return f'Enemy: {self.__color}. Location: ({self.__x},{self.__y})'

    def draw(self, display):
        '''
        Draws the Enemy on the screen.

        '''
        # the rectangular coordinates and size are stored in a variable
        # (https://www.pygame.org/docs/ref/rect.html)
        enemy_rect = pg.Rect(self.__coordinates, self.__size)
        # pygame draws the rectangle to the display
        pg.draw.rect(display, self.__color, enemy_rect)

    def move(self, left_bound, right_bound, top_bound, bottom_bound):
        """
        This method moves the enemy diagonally.

        Speed defined in an instance variable
        The enemy cannot move off the screen.
        The enemy should change direction when it reaches the edge of the screen.
        Take into account the size of the enemy.

        how are the bounds passed in?

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

# Getters, Setters and Property constructs made below

    @property
    def coordinates(self):
        '''
        Returns the coordinates of the Enemy.

        '''
        return self.__coordinates

    @coordinates.setter
    def coordinates(self, x=None, y=None):
        '''
        Sets the coordinates of the Enemy.

        '''
        if x is not None:
            self.__x = x
        if y is not None:
            self.__y = y

        self.__coordinates = [x, y]

    @property
    def size(self):
        '''
        Returns the size of the Enemy.

        '''
        return self.__size

    @size.setter
    def size(self, width=None, height=None):
        """
        This method sets the size of the enemy.

        """
        if width is not None:
            width = self.__width
        if height is not None:
            height = self.__height
            
        self.__size = [self.__width, self.__height]


    # def get_x(self):
    #     '''
    #     Returns the x coordinate of the Enemy.

    #     '''
    #     return self.__x

    # def set_x(self, x):
    #     '''
    #     Sets the x coordinate of the Enemy.

    #     '''
    #     self.__x = x

    # def get_y(self):
    #     '''
    #     Returns the y coordinate of the Enemy.

    #     '''
    #     return self.__y

    # def set_y(self, y):
    #     '''
    #     Sets the y coordinate of the Enemy.

    #     '''
    #     self.__y = y

    # def get_size(self):
    #     '''
    #     Returns the size of the Enemy.

    #     '''
    #     return self.__size

    # def set_size(self, size):
    #     '''
    #     Sets the size of the Enemy.

    #     '''
    #     self.__size = size if isinstance(size, list) else [size, size]

    # def get_color(self):
    #     '''
    #     Returns the color of the Enemy.

    #     '''
    #     return self.__color

    # def set_color(self, color):
    #     '''
    #     Sets the color of the Enemy.

    #     '''
    #     self.__color = color

    # def get_speed_x(self):
    #     '''
    #     Returns the speed of the Enemy in the x direction.

    #     '''
    #     return self.__speed_x

    # def set_speed_x(self, speed_x):
    #     '''
    #     Sets the speed of the Enemy in the x direction.

    #     '''
    #     self.__speed_x = speed_x

    # def get_speed_y(self):
    #     '''
    #     Returns the speed of the Enemy in the y direction.

    #     '''
    #     return self.__speed_y

    # def set_speed_y(self, speed_y):
    #     '''
    #     Sets the speed of the Enemy in the y direction.

    #     '''
    #     self.__speed_y = speed_y

    # x = property(get_x, set_x)
    # y = property(get_y, set_y)
    # size = property(get_size, set_size)
    # color = property(get_color, set_color)
    # speed_x = property(get_speed_x, set_speed_x)
    # speed_y = property(get_speed_y, set_speed_y)   
