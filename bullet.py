class Bullet:
    '''
    class for Bullet.

    The Bullet class contains the following variables, all of which should be private. You may decide
    whether the variables below are class or instance variables. However, you will need to defend your
    choice in your comments.
    (i) Variables for the coordinates of the bullet (including x, y, radius or size). Note that the
    bullet should not be initially visible on the screen
    (ii) Variables for the bullet colour
    (iii) Variables for the bullet speed
    (iv) A Boolean variable for determining whether the bullet is moving or not, initially set to
    False
    '''
    pass

    def __init__(self, width, height, color, speed):
        '''
        Constructor for the Bullet class.

        The constructor should be used to set up the Bullet class. This might include the coordinates,
        colour and speed of the Bullet as defined above

        The constructor should be used to set up the Bullet class. This might include the size, colour, speed
        of the Bullet as shown above. However, your implementation may be different depending on what
        shape you have decided to draw (e.g. a line, rectangle or circle)

        '''
        pass

    def __str__(self):
        '''
        Returns a string representation of the Bullet.

        This method should return a string representation of the Bullet.

        Create a string representation: You should ensure that when the object is printed to the screen, it
        contains reader-friendly information concerning the objects instance, including the color and
        position of the Bullet

        Create a string representation: when the object is printed to the screen, it should contain readerfriendly information concerning the object’s instance. This should include the colour and position of
        the Bullet
        '''
        pass

    def draw(self, display):
        '''
        Draws the Bullet on the screen.

        This method should draw the Bullet on the screen.

        This method should draw the Bullet on the screen.

        This method draw the bullet on the display window. The display window is passed in with this
        method. To draw the bullet, you will need to make use of pygame features (e.g. rectangle, circle or
        line). Note you should not need to draw the bullet in other methods
        '''
        pass

    def move_right(self):
        """
        This method moves the bullet right.

        This method should move the bullet right. Note that the bullet should not be able to move off the
        right of the screen.

        This method should move the bullet horizontally or vertically. The speed the bullet moves should be
        defined in an instance variable, created upon instantiation. Note the following constraints for the
        bullet:
        • The bullet should “emerge” from the shooter. Therefore, it should:
        • move horizontally, in the direction the enemy is located, if the shooter is located on the
        left/right hand side of the screen.
        • move vertically, in the direction the enemy is located, if the shooter is located on the
        top/bottom of the screen.
        • You do not need set the starting coordinates of the bullet here. This will be defined in the
        start() method below
        """
        pass

    def start(self, coordinates):
        """
        This method starts the bullet.

        This method should start the bullet moving. The bullet should be drawn on the screen and
        should be located at the coordinates passed in as a parameter.

        This method has been designed to be called when the user triggers the bullet to emerge from the
        shooter. Other than self, this method passes in the following parameters:
        • coordinates (sequence): a list or tuple determining the coordinates from which to start
        the bullet. You may assume the coordinates are in the correct format.
        This method should:
        • set the starting coordinates of the bullet; and
        • set the Boolean variable that determines whether the Bullet is moving to True
        """
        pass

    def stop(self):
        """
        This method stops the bullet.

        This method should stop the bullet from moving.

        This method stops the bullet from moving and causes the bullet to disappear from the display
        window. Therefore it should:
        • Set the coordinates of the bullet so that it is not visible on the display window
        • Set the instance variable that determines whether the bullet is moving to False
        """
        pass

    def check_moving(self):
        """
        This method checks whether the bullet is moving.

        This method should check whether the bullet is moving. If the bullet is moving, the method
        should return True. If the bullet is not moving, the method should return False.

        This method should return the value of the instance variable that determines whether the
        bullet is moving or not.

        This method should return:
        • True if the bullet is moving
        • False if the bullet is not moving
        """
        pass

    def wall_collision(self):
        """
        This method checks for a wall collision.

        If the bullet collides with the “wall” behind the enemy, it means that the bullet missed the enemy.
        This method should check if the bullet has collided with the wall behind the enemy. Depending on
        where your enemy is located, you may need to pass in an additional parameter to determine the
        wall location.
        • If the bullet has collided with the wall behind the enemy, the variable to control the bullet
        moving should be set to False. Additionally, the method should return True to determine
        that the bullet has collided with the wall.
        • If the bullet has not collided with the wall behind the enemy, the variable controlling the
        bullet moving should be set to True. Additionally, the method should return False to
        determine that the bullet has not collided with the wall.
        """
        pass

    def get_coordinates(self):
        """
        This method gets the coordinates of the bullet.

        This method should return the coordinates of the bullet.

        This method should return:
        • The coordinates of the bullet
        """
        pass

    def get_size(self):
        """
        This method gets the size of the bullet.

        This method should return the size of the bullet.

        This method should return:
        • The size of the bullet
        """
        pass

    def set_coordinates(self, coordinates):
        """
        This method sets the coordinates of the bullet.

        This method should set the coordinates of the bullet.

        This method should set the coordinates of the bullet.

        This method has been designed to be called when the bullet is moving. Other than self, this
        method passes in the following parameters:
        • coordinates (sequence): a list or tuple determining the coordinates to which to set the
        bullet. You may assume the coordinates are in the correct format.
        """
        pass

    def set_size(self, size):
        """
        This method sets the size of the bullet.

        This method should set the size of the bullet.

        This method should set the size of the bullet.

        This method has been designed to be called when the bullet is moving. Other than self, this
        method passes in the following parameters:
        • size (int): an integer determining the size to which to set the bullet.
        """
        pass



# When triggered, the bullet should appear from the shooter.
# Only one bullet should appear on the screen at a time.