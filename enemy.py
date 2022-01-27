class Enemy:
    '''
    class construct for drawing the Enemy.

    The Enemy class contains the following variables, all of which should be private. You may decide
    whether the variables below are class or instance variables. However, you will need to defend your
    choice in your comments.
    (i) Variables for the coordinates of the enemy (including x, y, radius or size in width/height)
    (ii) Variables for the enemy speed on the x and y axis
    '''
    pass

    def __init__(self, x, y, color, size, speed_x, speed_y):
        '''
        Constructor for the Enemy class.

        The constructor should be used to set up the Enemy class. This might include the coordinates,
        colour and speed of the Enemy as defined above
        Your implementation may be different, depending on
        which shape you decide to use

        size can be passed in as a list or a single value
        '''
        pass

    def __str__(self):
        '''
        Returns a string representation of the Enemy.

        This method should return a string representation of the Enemy.

        Create a string representation: You should ensure that when the object is printed to the screen, it
        contains reader-friendly information concerning the objects instance, including the color and
        position of the Enemy
        '''
        pass

    def draw(self, display):
        '''
        Draws the Enemy on the screen.

        This method should draw the Enemy on the screen.

        This method should draw the Enemy on the screen.

        This method draw the enemy on the display window. The display window is passed in with this
        method. To draw the enemy, you will need to make use of pygame features (e.g. rectangle, circle or
        line). Note you should not need to draw the enemy in other methods
        '''
        pass

    def move_left(self, left_bound, right_bound, top_bound, bottom_bound):
        """
        This method moves the enemy left.

        This method should move the enemy left or right, depending on which method you choose to
        implement. The speed the enemy moves should be defined in an instance variable, containing a
        value of your choice. Note the following constraints:
        • The enemy should not be able to move off the left of the screen OR the right of the screen
        (depending on which method has been implemented).
        • The enemy should not be able to move off the top of the screen OR the bottom of the screen
        (depending on which method has been implemented).
        Note that you should not draw the enemy in this method

        This method should move the enemy diagonally. The speed the enemy moves should be defined in
        instance variables, containing a value of your choice. Note the following constraints for the enemy:
        • The enemys movement should be constrained within the bounds defined in the parameters
        left_bound, right_bound, top_bound, bottom_bound.
        Therefore, the enemy should bounce (i.e. change direction) once it collides with the
        left_bound, right_bound, top_bound, or bottom_bound. You should take into account
        the size of the enemy when dealing with collisions
        """
        pass

    def get_x(self):
        '''
        Returns the x coordinate of the Enemy.

        This method should return the x coordinate of the Enemy.
        '''
        pass

    def get_y(self):
        '''
        Returns the y coordinate of the Enemy.

        This method should return the y coordinate of the Enemy.
        '''
        pass

    def get_size(self):
        '''
        Returns the size of the Enemy.

        This method should return the size of the Enemy.
        '''
        pass

    def set_x(self, x):
        '''
        Sets the x coordinate of the Enemy.

        This method should set the x coordinate of the Enemy.
        '''
        pass

    def set_y(self, y):
        '''
        Sets the y coordinate of the Enemy.

        This method should set the y coordinate of the Enemy.
        '''
        pass

    def set_size(self, size):
        '''
        Sets the size of the Enemy.

        This method should set the size of the Enemy.
        '''
        pass

# The enemy should be able to “bounce” off a protected wall, which is marked by an inner rectangle drawn inside of the screen (i.e. the pygame display window).
