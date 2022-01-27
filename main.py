import pygame

pygame.init()

# # Create a window (can I make it the size of the screen?)
DISPLAY_WIDTH = 500
DISPLAY_HEIGHT = 300
DISPLAY_SIZE = [DISPLAY_WIDTH, DISPLAY_HEIGHT]

display = pygame.display.set_mode(DISPLAY_SIZE)

run_game = True

clock = pygame.time.Clock()

black = [0, 0, 0]

while run_game:
    display.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False

    pygame.display.update()
    clock.tick(45)
pygame.quit()
quit()

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