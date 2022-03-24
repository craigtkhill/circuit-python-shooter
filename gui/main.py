import pygame as pg
from shooter import Shooter
from enemy import Enemy
from bullet import Bullet
from time import sleep
from math import sqrt

def check_collision(bullet, enemy):
    """
    Function to check if the bullet has collided with the enemy.

    """
    dist = sqrt((bullet.coordinate_x - enemy.coordinates_x)**2 + (bullet.coordinate_y - enemy.coordinates_y)**2)
    if dist <= bullet.width + enemy.width:
        return True
    return False

pg.init()

# The display width and height and stored in variables using multiple assignment
# https://stackoverflow.com/questions/5495332/more-elegant-way-of-declaring-multiple-variables-at-the-same-time
DISPLAY_WIDTH, DISPLAY_HEIGHT = 900, 600
# The display size is stored in a tuple
DISPLAY_SIZE = (DISPLAY_WIDTH, DISPLAY_HEIGHT)
# Pygame sets the display using the display size
DISPLAY = pg.display.set_mode(DISPLAY_SIZE)
# A caption is set for the game https://www.pygame.org/docs/ref/display.html#pygame.display.set_caption
pg.display.set_caption("Python Circuit Shooter")

# The background image is loaded
bg = pg.image.load("blits/space.jpg")

# Colors are assigned to RGB values in tuples
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (240, 210, 10)
RED = (250, 70, 90)
BLUE = (77, 150, 255)

# The boundary rectangle separating the shooter from the enemy is created using the following variables
BORDER_WIDTH = 1
BORDER_HEIGHT = DISPLAY_HEIGHT
# BORDER_X accounts for the width of the border
BORDER_X = DISPLAY_WIDTH // 2 - BORDER_WIDTH // 2
BORDER_Y = 0

# the rectangular coordinates and size are stored in a Rect object https://www.pygame.org/docs/ref/rect.html
# this represents a thin rectangle border separating the shooter and the enemy
BORDER = pg.Rect(BORDER_X, BORDER_Y, BORDER_WIDTH, BORDER_HEIGHT)

# Framerate is stored as a constant variable set to 60 frames per second
FPS = 60

# Shooter Variables
shooter_x = 100
shooter_y = 100
shooter_speed = 10
# a shooter is instantiated
shooter = Shooter(shooter_x, shooter_y, BLUE, shooter_speed)

# Enemy Variables
enemy_x = 400
enemy_y = 400
enemy_size = [25, 25]
enemy_speed_x = 10
enemy_speed_y = 10
# An enemy is instantiated
enemy = Enemy(enemy_x, enemy_y, RED, enemy_size, enemy_speed_x, enemy_speed_y)

# Bullet Variables
bullet_size = [10, 5]
bullet_speed = 50
# A bullet is instantiated
bullet = Bullet(bullet_size, YELLOW, bullet_speed)

# The left boundary for the enemy is the right of the rectangle border drawn in the center
# This rectangle object has an attribute 'right' that allows us to access the
# coordinate of the right side of the border
LEFT_BOUNDARY = BORDER.right
# The right boundary of the enemy is the width of the display
RIGHT_BOUNDARY = DISPLAY_WIDTH
# The top boundary for the enemy is zero
TOP_BOUNDARY = 0
# The bottom boundary for the enemy is the height of the display
BOTTOM_BOUNDARY = DISPLAY_HEIGHT

def draw_display():
    """
    Function to draw elements to the display.

    This helps to separate the drawing of elements from the logic
    of the game keeping the code cleaner and more readable.
    """
    # The display is cleared and the backgound filled with white.
    #DISPLAY.fill(WHITE)
    # The display is filled with an image of space
    DISPLAY.blit(bg, (0, 0))
    # A rectangle representing the boundary between the shooter and the enemy is drawn.
    pg.draw.rect(DISPLAY, BLACK, BORDER)
    # The shooter is drawn to the display.
    shooter.draw(DISPLAY)
    # The enemy is drawn to the display.
    enemy.draw(DISPLAY)
    # If the bullet is moving, it is drawn to the display.
    bullet.draw(DISPLAY)
    # The display is updated.
    pg.display.update()

def main():
    """
    Function to run the game and handle the games logic.
    """
    # a clock object is created to monitor the framerate
    clock = pg.time.Clock()
    # the run game variable is initially set to true
    run_game = True
    # While the game is running
    while run_game:
        # then all the elements are drawn to the display
        draw_display()
        # for every event in the event queue
        for event in pg.event.get():
        # if the user quits the game the run game is set to false.
            if event.type == pg.QUIT:
                run_game = False

        # Event driven programming is used to control the shooter.
        # When the user presses buttons such as the arrow keys (to move)
        # or the space bar (to shoot) the event is handled by the code which
        # responds to the event and changes the shooter's state or bullets state
        
        # the key.get_pressed() method provides a true value while the key is pressed
        # removing the need for an event loop checking the event type. 
        # The makes the code more readable and easier to understand.
        # https://stackoverflow.com/questions/66638465/whats-the-difference-betwen-pygame-key-get-pressed-and-event-type

        # A sequence of boolean values is created to store the keys pressed by the user 
        # using the pygame.key.get_pressed() function. 
        # http://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed
        keys_pressed = pg.key.get_pressed()
        # if the user is pressing the K_UP button the shooter is moved up
        shooter.move_up(keys_pressed)
        # if the user is pressing the K_DOWN button the shooter is moved down
        # the DISPLAY_HEIGHT argument prevents the shooter from moving below the bottom of the display.
        shooter.move_down(DISPLAY_HEIGHT, keys_pressed)
        # the enemy then moves diagonally from boundary to boundary with the boundary 
        # arguments preventing the enemy from moving outside the display.
        enemy.move(LEFT_BOUNDARY, RIGHT_BOUNDARY, TOP_BOUNDARY, BOTTOM_BOUNDARY)
        # if the user presses the space bar is pressed the bullet is fired
        if keys_pressed[pg.K_SPACE]:
            # a mask is made of the bullets coordinates taking into account the shooters
            # height and the bullet size.
            bullet_coordinates = [shooter.coordinates[0], shooter.coordinates[1] + shooter.height // 2 - bullet.height // 2]
            # this is used as the starting point for the bullet
            bullet.start(bullet_coordinates)
        # the bullet is moved right. This methods checks to see if the bullet is fired before moving.
        bullet.move_right()
        # if the bullet collides with the right boundary, it equates to true.
        if bullet.wall_collision(RIGHT_BOUNDARY):
            # in which case the bullets coordinates are reset and is_moving attribute is set to false
            bullet.stop()
        elif check_collision(bullet, enemy):
            bullet.stop()
            enemy.relocate(TOP_BOUNDARY, BOTTOM_BOUNDARY, LEFT_BOUNDARY, RIGHT_BOUNDARY)
            enemy.change_speed(1, 20)
            bullet.change_size(1, shooter.width)
            #sleep(0.3)
        # the clock is updated to the framerate
        clock.tick(FPS)
    # if user clicked the X on the screen the game is exited
    pg.quit()
    quit()

if __name__ == '__main__':
    main()