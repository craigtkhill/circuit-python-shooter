# getters and setters
# doctrings
# decorators / remove uncessary getters and setters
# capitalise classes

import pygame as pg
class Shooter:
    """
    A class to represent a shooter

    """

    def __init__(self, x, y, color, speed):
        '''
        Constructor for the Shooter class.
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
        Returns a string representation of the Shooter including its color and coordinates.

        '''
        return f'Shooter: {self.__color}. Location: ({self.__x},{self.__y})'

    def draw(self, display):
        '''
        Draws the Shooter on the screen.

        '''
        # the rectangular coordinates and size are stored in a variable
        # (https://www.pygame.org/docs/ref/rect.html)
        shooter_rect = pg.Rect(self.__coordinates, self.__size)
        # pygame draws the rectangle to the display
        pg.draw.rect(display, self.__color, shooter_rect)

    def move_up(self, moveup_trigger):
        """
        This method moves the shooter up.
        The shooter cannot move off the screen.

        a sequence of boolean values representing the state of every key on the keyboard
        Parameters
        ----------
            moveup_trigger : sequence of boolean values representing the state of the keys on the keyboard

        Returns
        -------
        
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
        This method moves the shooter down.
        The shooter cannot move off the screen.

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