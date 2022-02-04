import pygame as pg
class Shooter:
    """
    Class representing the shooter.

    Attributes
    ----------
        x : int
            the x coordinate of the shooter
        y : int
            the y coordinate of the shooter
        color : tuple
            the color of the shooter
        speed : int
            the speed of the shooter
    """

    def __init__(self, x, y, color, speed):
        '''
        Initializes the Shooter.

        Parameters
        ----------
            x : int
                the x coordinate of the shooter
            y : int
                the y coordinate of the shooter
            color : tuple or list
                the color of the shooter
            speed : int
                the speed of the shooter
        '''
        # Instance variable - multiple shooters can instantiated with different coordinates
        # allows flexibility if we want to introduce more shooters (multiplayer game)
        self.__x = x
        self.__y = y
        self.__coordinates = [self.__x, self.__y]
        # Instance variable as getters and setters can change the size of the individual Shooters
        self.__width = 20
        self.__height = 20
        self.__size = [self.__width, self.__height]
        # Instance variables - color and speed can be changed for each Shooter
        self.__color = color
        self.__speed = speed

    def __str__(self):
        '''
        A string representation of the Shooter including its color and location.
        '''
        return f'Shooter: {self.__color}. Location: ({self.__x},{self.__y})'

    def draw(self, display):
        '''
        Draws the Shooter on the screen.

        Parameters
        ----------
            display : pygame.display
                the display on which the shooter is drawn
        '''
        # the rectangular coordinates and size are stored in a variable
        # (https://www.pygame.org/docs/ref/rect.html)
        shooter_rect = pg.Rect(self.__coordinates, self.__size)
        # pygame draws the rectangle to the display
        pg.draw.rect(display, self.__color, shooter_rect)

    def move_up(self, moveup_trigger):
        """
        Moves the Shooter up.

        Parameters
        ----------
            moveup_trigger : pygame.key.get_pressed()
                the state of the keys on the keyboard        
        """
        # if the up arrow is pressed the y coordinate instance variable is reversed
        # by reassigning it to the value of itself minus the speed
        if moveup_trigger[pg.K_UP]:
            self.__y -= self.__speed
        # if the y coordinate is less than zero, the y coordinate is set to 0
        # preventing the shooter from going off the screen
            if self.__y < 0:
                self.__y = 0
        # the coordinates of the shooter are updated with the new value for y
            self.__coordinates = [self.__x, self.__y]

    def move_down(self, display_height, movedown_trigger):
        """
        Moves the Shooter down.

        Parameters
        ----------

            display_height : int
                the height of the display
            movedown_trigger : pygame.key.get_pressed()
                the state of the keys on the keyboard
        """
        # if the down arrow is pressed the y coordinate instance variable is increased
        # by reassigning it to the value of itself plus the speed
        if movedown_trigger[pg.K_DOWN]:
            self.__y += self.__speed
        # if the y coordinate is less greater than the height of the display
        # taking into account its height, the y coordinate is set to the height of
        # the display, minus its own height
            if self.__y > display_height - self.__height:
                self.__y = display_height - self.__height
        # the coordinates of the shooter are updated with the new value for y 
            self.__coordinates = [self.__x, self.__y]

# Getters, Setters and Property constructs made below
####### WHAT ARE THE ADVANTAGES OF DECORATORS?
# (https://stackoverflow.com/questions/52899509/is-there-an-advantage-of-using-the-property-decorator-compared-to-the-property-c)

    @property
    def coordinates(self):
        """
        Gets the coordinates of the shooter.

        Returns
        -------
            coordinates : list
                the coordinates of the shooter
        """
        return self.__coordinates

# (https://stackoverflow.com/questions/7371244/using-self-as-default-value-for-a-method)

    @coordinates.setter
    def coordinates(self, x=None, y=None):
        """
        Sets the coordinates of the shooter.

        Parameters
        ----------
            x : int
                the x coordinate of the shooter
            y : int
                the y coordinate of the shooter
        """
        if x is not None:
            x = self.__x
        if y is not None:
            y = self.__y

        self.__coordinates = [self.__x, self.__y]

    @property
    def size(self):
        """
        Gets the size of the shooter.

        Returns
        -------
            size : list
                the size of the shooter
        """
        return self.__size

    @size.setter
    def size(self, width=None, height=None):
        """
        This method sets the size of the shooter.

        Parameters
        ----------
            width : int
                the width of the shooter
            height : int
                the height of the shooter
        """
        if width is not None:
            width = self.__width
        if height is not None:
            height = self.__height
            
        self.__size = [self.__width, self.__height]