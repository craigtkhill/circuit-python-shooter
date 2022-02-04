import pygame as pg
from shooter import Shooter
from enemy import Enemy
from bullet import Bullet

pg.init()

# The display width and height and stored in variables using multiple assignment
# (https://stackoverflow.com/questions/5495332/more-elegant-way-of-declaring-multiple-variables-at-the-same-time)
DISPLAY_WIDTH, DISPLAY_HEIGHT = 900, 600
# The display size is stored in a tuple
DISPLAY_SIZE = (DISPLAY_WIDTH, DISPLAY_HEIGHT)
# Pygame sets the display using the display size
DISPLAY = pg.display.set_mode(DISPLAY_SIZE)
# A caption is set for the game 
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
    Function to draw elements the window.
    """
    DISPLAY.fill(WHITE) # 90 minute video for beginners
    # HERE I DRAW TO THE SCREEN
    pg.draw.rect(DISPLAY, GREY, BORDER)
    shooter.draw(DISPLAY)
    enemy.draw(DISPLAY)
    bullet.draw(DISPLAY)
    pg.display.update()

def main():
    """
    Function to run the game.
    """
    clock = pg.time.Clock()
    run_game = True
    while run_game:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run_game = False

        keys_pressed = pg.key.get_pressed()
        shooter.move_up(keys_pressed)
        shooter.move_down(DISPLAY_HEIGHT, keys_pressed)
        enemy.move(LEFT_BOUNDARY, RIGHT_BOUNDARY, TOP_BOUNDARY, BOTTOM_BOUNDARY)
        if keys_pressed[pg.K_SPACE]:
            bullet.start(shooter.coordinates)
        bullet.move_right()
        if bullet.wall_collision(RIGHT_BOUNDARY):
            bullet.stop()

        draw_window()
    pg.quit()
    quit()

if __name__ == '__main__':
    main()