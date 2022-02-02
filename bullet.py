# make a line for the bullet
# move right check if it is off the screen
# how to make bullet invisible on the screen
# check the bullet is moving before setting
# decorators / remove uncessary getters and setters
import pygame as pg

class Bullet:
    '''
    Class representing the Bullet.

    '''

    def __init__(self, size, color, speed):
        '''
        Constructor for the Bullet class.

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
        Returns a string representation of the Bullet.

        '''
        return f'Bullet: {self.__color}. Location: ({self.__x, self.__y})'

    def draw(self, display):
        '''
        Draws the Bullet on the screen.

        '''
        # the rectangular coordinates and size are stored in a variable
        # (https://www.pygame.org/docs/ref/rect.html)
        bullet_rect = pg.Rect(self.__coordinates, self.__size)
        # pygame draws the rectangle to the display
        pg.draw.rect(display, self.__color, bullet_rect)

    def move_right(self):
        """
        This method moves the bullet right.

        The bullet not be able to move off the screen. Therefore, this method should check if the bullet is able to move right.

        The bullet should “emerge” from the shooter. Therefore, it should:
        move horizontally, in the direction the enemy is located, if the shooter is located on the left/right hand side of the screen.
        starting coordinates in the start method.
        """
        self.__x += self.__speed
        self.__coordinates = [self.__x, self.__y]


    def start(self, coordinates):
        """
        Starts the bullet moving and causes the bullet to appear on the screen.

        coordinates (sequence): a list or tuple determining the coordinates from which to start the bullet. You may assume the coordinates are in the correct format.
        set the Boolean variable that determines whether the Bullet is moving to True
        """
        # the starting coordinates of the bullet are assigned
        self.__x = coordinates[0]
        self.__y = coordinates[1]
        self.__coordinates = [self.__x, self.__y]
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
        self.coordinates = [0, 0]

    def check_moving(self):
        """
        This method checks whether the bullet is moving.

        """
        return self.__moving

    def wall_collision(self, right_bound):
        """
        This method checks for a wall collision.

        If the bullet collides with the “wall” behind the enemy, it means that the bullet missed the enemy.
        This method should check if the bullet has collided with the wall behind the enemy. Depending on where your enemy is located, you may need to pass in an additional parameter to determine the wall location.
        • If the bullet has collided with the wall behind the enemy, the variable to control the bullet moving should be set to False. Additionally, the method should return True to determine that the bullet has collided with the wall.
        • If the bullet has not collided with the wall behind the enemy, the variable controlling the bullet moving should be set to True. Additionally, the method should return False to determine that the bullet has not collided with the wall.
        """
        # if the x coordinate of the bullet is less than or equal to the right bound
        # False is returned
        if self.__coordinates[0] <= right_bound:
            return False
        # Otherwise, the moving variable is set to False and True is returned
        self.__moving = False
        return True

# Getters, Setters and Property constructs made below

    def get_x(self):
        '''
        Returns the x coordinate of the Bullet.

        '''
        return self.__x

    def set_x(self, x):
        '''
        Sets the x coordinate of the Bullet.

        '''
        self.__x = x

    def get_y(self):
        '''
        Returns the y coordinate of the Bullet.

        '''
        return self.__y

    def set_y(self, y):
        '''
        Sets the y coordinate of the Bullet.

        '''
        self.__y = y

    def get_coordinates(self):
        """
        This method gets the coordinates of the bullet.

        """
        return self.__coordinates

    def set_coordinates(self, coordinates):
        """
        This method sets the coordinates of the bullet.

        This method has been designed to be called when the bullet is moving. Other than self, this method passes in the following parameters:
        coordinates (sequence): a list or tuple determining the coordinates to which to set the bullet. You may assume the coordinates are in the correct format.
        """
        if self.check_moving():
            self.__coordinates = coordinates

    def get_size(self):
        """
        This method gets the size of the bullet.

        """
        return self.__size

    def set_size(self, size):
        """
        This method sets the size of the bullet.

        This method has been designed to be called when the bullet is moving. Other than self, this method passes in the following parameters:
        size (int): an integer determining the size to which to set the bullet.
        """
        if self.check_moving():
            self.__size = size if isinstance(size, list) else [size, size]
    
    def get_color(self):
        """
        This method gets the color of the bullet.

        """
        return self.__color

    def set_color(self, color):
        """
        This method sets the color of the bullet.
        color (sequence): a sequence determining the color to which to set the bullet. You may assume the color is in the correct format.
        """
        if self.check_moving():
            self.__color = color

    def get_speed(self):
        """
        This method gets the speed of the bullet.

        """
        return self.__speed

    def set_speed(self, speed):
        """
        This method sets the speed of the bullet.
        
        """
        if self.check_moving():
            self.__speed = speed

    coordinates = property(get_coordinates, set_coordinates)
    size = property(get_size, set_size)
    color = property(get_color, set_color)
    speed = property(get_speed, set_speed)