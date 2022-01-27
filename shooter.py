class Shooter:
    '''
    class for Shooter. Your Shooter can be a shape of
    your choice.

    The Shooter class contains the following variables, all of which should be private. You may decide
    whether the variables below are class or instance variables. However, you will need to defend your
    choice in your comments.
    (i) Variables for the coordinates of the shooter (
    '''
    pass

    def __init__(self, x, y, color, speed):
        '''
        Constructor for the Shooter class.

        The constructor should be used to set up the Shooter class. This might include the coordinates,
        colour and speed of the Shooter as defined above
        '''
        pass

    def __str__(self):
        '''
        Returns a string representation of the Shooter.

        This method should return a string representation of the Shooter.

        Create a string representation: when the object is printed to the screen, it should contain readerfriendly information concerning the objects instance. This should include the colour and coordinates of the Shooter
        '''
        pass

    def draw(self, display):
        '''
        Draws the Shooter on the screen.

        This method should draw the Shooter on the screen.

        This method should draw the Shooter on the screen.

        This method draw the shooter on the display window. To draw the shooter, you will need to make
        use of pygame features (e.g. rectangles, circles, lines). Note you should not need to draw the
        shooter in other methods.
        '''
        pass

    def move_up(self, moveup_trigger):
        """
        This method moves the shooter up.

        This method should move the shooter left or up, depending on which method you choose to
        implement. The speed the shooter moves should be defined in an instance variable, containing a
        value of your choice. Note the following constraints:
        • The shooter should not be able to move off the left of the screen OR the top of the screen
        (depending on which method has been implemented).
        Note that you should not draw the shooter in this method
        
        """
        pass

    def move_down(self, movedown_trigger):
        """
        This method should move the shooter right or down, depending on which method you choose to
        implement. The speed the shooter moves should be defined in an instance variable, containing a
        value of your choice. Note the following constraints:
        • The shooter should not be able to move off the right of the screen OR the bottom of the
        screen (depending on which method has been implemented).
        Note that you should not draw the shooter in this method.

        """
        pass

    def get_x(self):
        """
        This method returns the x coordinate of the shooter.

        This method should return the x coordinate of the shooter.
        """
        pass

    def get_y(self):
        """
        This method returns the y coordinate of the shooter.

        This method should return the y coordinate of the shooter.
        """
        pass

    def set_x(self, x):
        """
        This method sets the x coordinate of the shooter.

        This method should set the x coordinate of the shooter.
        """
        pass

    def set_y(self, y):
        """
        This method sets the y coordinate of the shooter.

        This method should set the y coordinate of the shooter.
        """
        pass

    def get_color(self):
        """
        This method returns the colour of the shooter.

        This method should return the colour of the shooter.
        """
        pass

    def set_color(self, color):
        """
        This method sets the colour of the shooter.

        This method should set the colour of the shooter.
        """
        pass

    

# The shooter should only be able to move horizontally OR vertically. It should not move in both
# directions.
# The shooter should not be able to move outside the bounds of the window/screen.
# The shooter should not be able to move off the screen