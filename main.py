# continue commenting from the boundary.right etc
# check I met all the requirements on the sheet

# Import the libaries necessary
import pygame as pg
from shooter import Shooter
from enemy import Enemy
from bullet import Bullet

pg.init()

# The display width and height and stored in variables using multiple assignment
# (https://stackoverflow.com/questions/5495332/more-elegant-way-of-declaring-multiple-variables-at-the-same-time)
# Uppercase indicates constants whos values will not change while the program is running
DISPLAY_WIDTH, DISPLAY_HEIGHT = 900, 600
# Then the display size is stored in a tuple
DISPLAY_SIZE = (DISPLAY_WIDTH, DISPLAY_HEIGHT)
# Pygame then sets the display using the display size
DISPLAY = pg.display.set_mode(DISPLAY_SIZE)
# and a caption is set for the game
# (https://www.pygame.org/docs/ref/display.html#pygame.display.set_caption)
pg.display.set_caption("Shooter")

# Colors are assigned in tuples
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREY = (251, 248, 241)

# The boundary rectangle separating the shooter from the enemy is created using the following variables
BORDER_WIDTH = 10
BORDER_HEIGHT = DISPLAY_HEIGHT
# border x accounts for the width of the border
BORDER_X = DISPLAY_WIDTH // 2 - BORDER_WIDTH // 2
BORDER_Y = 0

# the rectangular coordinates and size are stored in a variable
# (https://www.pygame.org/docs/ref/rect.html)
BORDER = pg.Rect(BORDER_X, BORDER_Y, BORDER_WIDTH, BORDER_HEIGHT)

# Framerate is stored as a constant variable
FPS = 60

# Shooter Variables
shooter_x = 100
shooter_y = 100
shooter_speed = 5
# a shooter is instanced
shooter = Shooter(shooter_x, shooter_y, BLACK, shooter_speed)

# Enemy Variables
enemy_x = 400
enemy_y = 400
enemy_size = [20, 30]
enemy_speed_x = 10
enemy_speed_y = 10
# a enemy is instanced
enemy = Enemy(enemy_x, enemy_y, YELLOW, enemy_size, enemy_speed_x, enemy_speed_y)

# Bullet Variables
bullet_size = [10, 5]
bullet_speed = 20
bullet = Bullet(bullet_size, RED, bullet_speed)

# Available to us because of the Rect object
LEFT_BOUNDARY = BORDER.right
RIGHT_BOUNDARY = DISPLAY_WIDTH
TOP_BOUNDARY = 0
BOTTOM_BOUNDARY = DISPLAY_HEIGHT

def draw_window():
    """
    Method to draw the window.
    """
    DISPLAY.fill(WHITE) # 90 minute video for beginners
    # HERE I DRAW TO THE SCREEN
    pg.draw.rect(DISPLAY, GREY, BORDER)
    shooter.draw(DISPLAY)
    enemy.draw(DISPLAY)
    if bullet.check_moving():
        bullet.draw(DISPLAY)
    pg.display.update()

def main():
    clock = pg.time.Clock()
    run_game = True
    while run_game:
        clock.tick(FPS) # do I do this at the start of the end?
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run_game = False

        keys_pressed = pg.key.get_pressed()
        shooter.move_up(keys_pressed)
        shooter.move_down(DISPLAY_HEIGHT, keys_pressed)
        enemy.move(LEFT_BOUNDARY, RIGHT_BOUNDARY, TOP_BOUNDARY, BOTTOM_BOUNDARY)
        if not bullet.check_moving() and keys_pressed[pg.K_SPACE]:
            bullet.start(shooter.coordinates)
        if bullet.check_moving():
            bullet.move_right()
        if bullet.wall_collision(RIGHT_BOUNDARY):
            bullet.stop()

        draw_window()
    pg.quit()
    quit()

def test():
    print(shooter)

if __name__ == '__main__':
    main()
    #test()

# test all my getters and setters

# draw a rectangle that marks the boundary of the screen

# The enemy should be able to move diagonally and should automatically move. Appropriate
# methods should be called so that the enemy collides with the “walls” of the rectangle you have
# drawn to the screen (above). 

# left and right, with the left and right arrow keys on the keyboard respectively; or
# b) Up and down, with the up and down arrow keys on the keyboard respectively.
# The implementation of either (a) or (b) depends on how you decide the user should
# interact with the game.
# The shooter should not move off the screen. The shooter should continue moving when
# the user has the appropriate key pressed, and stop moving once released.

# When a user presses a key of your choice (other than the keys already in use for the
# application), a bullet should appear from the shooter and move horizontally or vertically,
# depending on the location of the shooter. Note that:
# § No more than one bullet should appear at a time. The shooter cannot launch another
# bullet until the original bullet launched has disappeared off the screen

# The game should continue to play and the display window should remain open, until the user
# closes the window by clicking the “x” on the top corner of the screen.


#####################################
# DEFINITION OF GAME CLASSES

# Pygame is imported and used appropriately to
# draw shapes or images for the bullet, shooter
# and enemy.
# The methods inside the Bullet, Shooter and
# Enemy class are defined and working correctly.
# There are no issues with the code and
# everything works as described.

# Comments: The student explains what the
# methods are doing in their own words,
# demonstrating clear understanding. The
# student also explains in the comments how
# each class is designed both draw and
# manipulate the objects as separate GUI
# components using their own words.

# GAME PLAY INTERACTIONS

# The Bullet, Shooter and Enemy classes are
# imported in main.py. Instances of the class are
# created.
# All pygame elements described are working.
# The objects (shooter/bullet/enemy/rectangle)
# are drawn to the screen. Objects are moving
# and working as described. Event driven
# programming is applied to control object
# movements and collisions, where necessary.
# Comments: the student explains, in their own
# words, what the pygame interactions are doing.
# The student explains event driven
# programming, and how it was employed to
# control each of the objects created in their own
# words

# double check everything with the pdf to make sure I missed nothing