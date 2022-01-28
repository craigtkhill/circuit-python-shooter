import pygame as pg

class Bullet:
    '''
    Class representing the Bullet.

    '''

    def __init__(self, x, y, size, color, speed):
        '''
        Constructor for the Bullet class.

        '''
        self.__x = x
        self.__y = y
        # commment again
        self.__size = size if isinstance(size, list) else [size, size]
        self.__color = color
        self.__speed = speed
        self.__moving = False
        self.__coordinates = [x, y]

    def __str__(self):
        '''
        Returns a string representation of the Bullet.

        '''
        return f'Bullet: {self.__color}. Location ({self.__x, self.__y})'

    def draw(self, display):
        '''
        Draws the Bullet on the screen.

        '''
        pg.draw.rect(display, self.__color, (self.__coordinates, self.__size))

    def move_right(self):
        """
        This method moves the bullet right.

        The bullet not be able to move off the screen. Therefore, this method should check if the bullet is able to move right.

        The bullet should “emerge” from the shooter. Therefore, it should:
        move horizontally, in the direction the enemy is located, if the shooter is located on the left/right hand side of the screen.
        starting coordinates in the start method.
        """
        pass

    def start(self, coordinates):
        """
        Starts the bullet moving and causes the bullet to appear on the screen.

        coordinates (sequence): a list or tuple determining the coordinates from which to start the bullet. You may assume the coordinates are in the correct format.
        set the Boolean variable that determines whether the Bullet is moving to True
        """
        pass

    def stop(self):
        """
        Stops the bullet from moving and causes the bullet to disappear from the display. 
        Set the coordinates of the bullet so that it is not visible on the display window
        Set the instance variable that determines whether the bullet is moving to False
        """
        pass

    def check_moving(self):
        """
        This method checks whether the bullet is moving.

        """
        return self.__moving

    def wall_collision(self):
        """
        This method checks for a wall collision.

        If the bullet collides with the “wall” behind the enemy, it means that the bullet missed the enemy.
        This method should check if the bullet has collided with the wall behind the enemy. Depending on where your enemy is located, you may need to pass in an additional parameter to determine the wall location.
        • If the bullet has collided with the wall behind the enemy, the variable to control the bullet moving should be set to False. Additionally, the method should return True to determine that the bullet has collided with the wall.
        • If the bullet has not collided with the wall behind the enemy, the variable controlling the bullet moving should be set to True. Additionally, the method should return False to determine that the bullet has not collided with the wall.
        """
        pass

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

# When triggered, the bullet should appear from the shooter.
# Only one bullet should appear on the screen at a time.