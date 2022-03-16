import pygame as pg
from random import randint

class Bullet:
    '''
    Class representing the bullet.

    Attributes
    ----------
        x : int
            the x coordinate of the bullet
        y : int
            the y coordinate of the bullet
        size : tuple, list or int
            the height and width of the bullet
        color : tuple or list of RGB values
            the color of the bullet
        speed : int
            the speed of the bullet
        moving : bool
            True if the bullet is moving, False otherwise
    '''

    def __init__(self, size, color, speed):
        '''
        Initializes the Bullet.

        Currently there is only one bullet allowed on the screen at a time however 
        Using instance variables allows flexibility to introduce multiple bullets later if we wish. We may also want to extend the code to different types of bullets
        with different sizes, colors and speeds.
        '''
        self.__x = 0
        self.__y = 0
        self.__coordinates = [self.__x, self.__y]
        # if the size parameter is a list or tuple the values in the are assigned
        # to the size of the bullet, otherwise and new list with two values 
        # is created using a simplied if else statement
        # (https://docs.python.org/3/library/functions.html#isinstance)
        # (https://stackoverflow.com/questions/2802726/putting-a-simple-if-then-else-statement-on-one-line)
        self.__size = size if isinstance(size, list) else [size, size]
        self.__color = color
        self.__speed = speed
        self.__moving = False
        

    def __str__(self):
        '''
        Returns a string representation of the bullet including color and location.

        '''
        return f'Bullet: {self.__color}. Location: ({self.__x, self.__y})'

    def draw(self, display):
        '''
        Draws the Bullet on the screen.

        Parameters
        ----------
            display : pygame.display
                the display window

        Precondition: The bullet is moving.
        '''
        # the rectangular coordinates and size are stored in a variable
        # (https://www.pygame.org/docs/ref/rect.html)
        bullet_rect = pg.Rect(self.__coordinates, self.__size)
        # if the bullet has been fired
        if self.check_moving():
            # pygame draws the rectangle to the display
            pg.draw.rect(display, self.__color, bullet_rect)

    def move_right(self):
        """
        Moves the bullet right.

        Precondition: The bullet is moving.
        """
        # if the bullet is moving
        if self.check_moving():
        # the x coordinate of the bullet is incremented by the speed
            self.__x += self.__speed
            # and the coordinates of the bullet are updated
            self.__coordinates = [self.__x, self.__y]


    def start(self, coordinates):
        """
        Starts the bullet moving if there are no other bullets on the screen.
        Sets the bullets moving attribute to True.

        Parameters
        ----------
            coordinates : list
                the coordinates of the bullet

        Precondition: The bullet is not moving.
        """
        # if there is no bullet on the screen
        if self.check_moving() == False:
        # the starting coordinates of the bullet are assigned
            self.__x = coordinates[0]
            self.__y = coordinates[1]
            # and the moving variable is set to true
            self.__moving = True

    def stop(self):
        """
        Stops the bullet from moving and resets the bullet's coordinates.
        """
        # the moving variable is set to false
        self.__moving = False
        # the coordinates are reset to 0, 0
        self.__coordinates = [0, 0]

    def check_moving(self):
        """
        This method checks whether the bullet is moving.

        """
        return self.__moving

    def wall_collision(self, right_bound):
        """
        Checks if the bullet collided with the wall.
        Sets the bullets moving attribute to false if it did.

        Parameters
        ----------
            right_bound : int
                the right bound of the screen

        Returns
        -------
            bool
                True if the bullet collided with the wall, else False        
        """
        # if the x coordinate of the bullet is less than or equal to the right bound
        # False is returned
        if self.__coordinates[0] <= right_bound:
            return False
        # Otherwise, the moving variable is set to False and True is returned
        self.__moving = False
        return True
    
    def change_size(self, lower_limit, upper_limit):
        """
        Changes the width of the Bullet

        Parameters
        ----------
            lower_limit : int
                the lower limit of the size
            upper_limit : int
                the upper limit of the size
        """
        # the width of the bullet is randomly generated within the bounds
        self.__size[1] = randint(lower_limit,upper_limit)

# Getters for coordinates and size of the bullet below.

    @property
    def coordinates(self):
        '''
        Gets the coordinates of the bullet.

        Returns
        -------
            coordinates : list
                the x and y coordinates of the bullet
        '''
        return self.__coordinates

    @property
    def height(self):
        '''
        Gets the size of the bullet.

        Returns
        -------
            size : int
                the height of the bullet
        '''
        return self.__size[1]

    @property
    def width(self):
        '''
        Gets the width of the bullet.

        Returns
        -------
            size : int
                the width of the bullet
        '''
        return self.__size[0]

