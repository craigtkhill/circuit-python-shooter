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
        color : tuple or list of RGB values
            the color of the shooter
        speed : int
            the speed of the shooter
    """

    def __init__(self, x, y, color, speed):
        '''
        Initializes the Shooter.

        Instance variables are used here to allow multiple shooters to be instantiated 
        with different coordinates, sizes, colors and speeds set individually.
        This allows flexibility if we want to introduce more shooters (multiplayer game)
        '''
        # Coordinates
        self.__x = x
        self.__y = y
        self.__coordinates = [self.__x, self.__y]
        # Size
        self.__width = 30
        self.__height = 20
        self.__size = [self.__width, self.__height]
        # Color
        self.__color = color
        # Speed
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
        # the rectangular coordinates and size are stored in a Rect Object
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
        # if the up arrow is pressed the y coordinate instance variable is decreased
        # by reassigning it to the value of itself minus the speed
        if moveup_trigger[pg.K_UP]:
            self.__y -= self.__speed
        # to prevent the shooter from going off the screen
        # if the y coordinate is less than zero, the y coordinate is set to 0
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
        # if the y coordinate is greater than the height of the display
        # taking into account its height, the y coordinate is set to the height of
        # the display, minus its own height
            if self.__y > display_height - self.__height:
                self.__y = display_height - self.__height
        # the coordinates of the shooter are updated with the new value for y 
            self.__coordinates = [self.__x, self.__y]

# Getters for coordinates and size of the shooter below.
# using the property decorator is best practice as it can prevent bugs and refactoring issues further down the line. https://stackoverflow.com/questions/52899509/is-there-an-advantage-of-using-the-property-decorator-compared-to-the-property-c

    @property
    def coordinates(self):
        """
        Gets the coordinates of the shooter.

        Returns
        -------
            coordinates : list
                the x and y coordinates of the shooter
        """
        return self.__coordinates

    @property
    def height(self):
        """
        Gets the height of the shooter.

        Returns
        -------
            height :int
                the height of the shooter
        """
        return self.__height
        
    @property
    def width(self):
        """
        Gets the width of the shooter.

        Returns
        -------
            width :int
                the width of the shooter
        """
        return self.__width
    