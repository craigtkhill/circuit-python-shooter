import pygame as pg

class Bullet:
    '''
    Class representing the bullet.

    Attributes
    ----------
        x : int
            the x coordinate of the bullet
        y : int
            the y coordinate of the bullet
        size : tuple/list of int or int
            the size of the bullet
        color : tuple, list or int 
            the color of the bullet
        speed : int
            the speed of the bullet
        moving : bool
            True if the bullet is moving, False otherwise
    '''

    def __init__(self, size, color, speed):
        '''
        Initializes the Bullet.

        Parameters
        ----------
            size : list
                the size of the bullet
            color : tuple, list or int
                the color of the bullet
            speed : int
                the speed of the bullet

        '''
        # Instance Variable - Currently there is only one bullet allowed on the
        # screen at a time however instance variables allow flexibility
        # to introduce multiple bullets later if we wish.
        self.__x = 0
        self.__y = 0
        self.__coordinates = [self.__x, self.__y]
        # Instance Variables - The colors, sizes, speeds and is_moving for each bullet can be set individually
        # if the size parameter is a list the values in the list are assigned
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
        '''
        # if the bullet has been fired
        if self.check_moving():
        # the rectangular coordinates and size are stored in a variable
        # (https://www.pygame.org/docs/ref/rect.html)
            bullet_rect = pg.Rect(self.__coordinates, self.__size)
            # pygame draws the rectangle to the display
            pg.draw.rect(display, self.__color, bullet_rect)

    def move_right(self):
        """
        Moves the bullet right.

        Precondition: The bullet is moving.
        """
        if self.check_moving():
            self.__x += self.__speed
            self.__coordinates = [self.__x, self.__y]


    def start(self, coordinates):
        """
        Starts the bullet moving and causes the bullet to appear on the screen.

        Parameters
        ----------
            coordinates : list
                the coordinates of the bullet
        """
        # if there is no bullet on the screen
        if self.check_moving() == False:
        # the starting coordinates of the bullet are assigned
            self.__x = coordinates[0]
            self.__y = coordinates[1]
            #self.__coordinates = [self.__x, self.__y]
            # and the moving variable is set to true
            self.__moving = True

    def stop(self):
        """
        Stops the bullet from moving and causes the bullet to disappear from the display. 
        Set the coordinates of the bullet so that it is not visible on the display window
        Set the instance variable that determines whether the bullet is moving to False
        """
        # the moving variable is set to false
        self.__moving = False
        # and the coordinates are reset to 0, 0
        self.__coordinates = [0, 0]

    def check_moving(self):
        """
        This method checks whether the bullet is moving.

        """
        return self.__moving

    def wall_collision(self, right_bound):
        """
        Checks if the bullet collided with the wall.

        Parameters
        ----------
            right_bound : int
                the right bound of the screen

        Returns
        -------
            bool
                True if the bullet collided with the wall, False otherwise        
        """
        # if the x coordinate of the bullet is less than or equal to the right bound
        # False is returned
        if self.__coordinates[0] <= right_bound:
            return False
        # Otherwise, the moving variable is set to False and True is returned
        self.__moving = False
        return True

    @property
    def coordinates(self):
        '''
        Gets the coordinates of the bullet.

        Returns
        -------
            coordinates : list of int
                the coordinates of the bullet
        '''
        return self.__coordinates

    @coordinates.setter
    def coordinates(self, x=None, y=None):
        '''
        Sets the coordinates of the bullet.

        Parameters
        ----------
            x : int
                the x coordinate of the bullet
            y : int
                the y coordinate of the bullet
        '''
        if x is not None:
            self.__x = x
        if y is not None:
            self.__y = y

        self.__coordinates = [self.__x, self.__y]

    @property
    def size(self):
        '''
        Gets the size of the bullet.

        Returns
        -------
            size : list of int
                the size of the bullet
        '''
        return self.__size

    @size.setter
    def size(self, size):
        """
        Sets the size of the bullet.

        Parameters
        ----------
            size : tuple/list of int or int
                the size of the bullet
        """
        self.__size = size if isinstance(size, list) else [size, size] 