import pygame as pg
from shooter import Shooter
from enemy import Enemy
from bullet import Bullet

pg.init()

# # Create a window (can I make it the size of the screen?)
DISPLAY_WIDTH, DISPLAY_HEIGHT = 900, 600
DISPLAY_SIZE = (DISPLAY_WIDTH, DISPLAY_HEIGHT)
DISPLAY = pg.display.set_mode(DISPLAY_SIZE)
pg.display.set_caption("Shooter")

# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Border
BORDER = pg.Rect(DISPLAY_WIDTH // 2 - 5, 0, 10, DISPLAY_HEIGHT) # 90 minute video for beginners

# Framerate
FPS = 60

# Shooter Variables

shooter = Shooter(100,100, BLACK, 5)

# Enemy Variables
enemy = Enemy(500,100, BLACK, [20, 30], 10, 10)

# Bullet Variables
bullet = Bullet([10,5], RED, 20)

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
    pg.draw.rect(DISPLAY, WHITE, BORDER)
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
        shooter.move_down(keys_pressed)
        enemy.move(LEFT_BOUNDARY, RIGHT_BOUNDARY, TOP_BOUNDARY, BOTTOM_BOUNDARY)
        if not bullet.check_moving() and keys_pressed[pg.K_SPACE]:
            bullet.start(shooter.coordinates)
        if bullet.check_moving():
            bullet.move_right()
        if bullet.wall_collision():
            bullet.stop()

        draw_window()
    pg.quit()
    quit()

if __name__ == '__main__':
    main()

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