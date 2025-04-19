import pygame
from constants import *

def find_square(x, y, squares):
    #function to define where the player clicked and return the correct square, button or missclick
    pass


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pass
    doing = {}

    doing["player"] = player_go
    doing["pen"] = pen_mode
    doing["pencil"] = pencil_mode
    doing["clicked out"] = print

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    tiros = pygame.sprite.Group()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
            # check if the mouse is pressed and where
                x, y = event["pos"]
            # use function accordingly to dict if mouse pressed
                doing[find_square(x,y)]
            if event.type == pygame.QUIT:
                return


if __name__ == "__main__":
    main()