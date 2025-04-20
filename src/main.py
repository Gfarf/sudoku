import pygame
from constants import *

def find_square(x, y, board):
    #function to define where the player clicked and return the correct square, button or missclick
    if y > 590:
    #tested if in board or buttons region, then test each button if in button region
        if (x < 331 and x > 29) and (y > 599 and y < 701):
            MODE = "pen"
        if (x < 691 and x > 389) and (y > 599 and y < 701):
            MODE = "pencil"
        return
    board.find(x, y)
    
    
    pass


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    mode = "pen"
    pass
# making a dictionary of functions to deal with the mouse click

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
            # check if the mouse is pressed and where
                x, y = event["pos"]
            # move player or change mode accordingly to where was the pressed mouse button
                if y > FLOOR:
                #tested if in board or buttons region, then test each button if in button region
                    if (x <= (BUTTON_WIDTH + BUTTON_X_MARGIN) and x >= BUTTON_X_MARGIN) and (y >= (FLOOR + BUTTON_Y_MARGIN) and y <= (FLOOR + BUTTON_Y_MARGIN + BUTTON_HEIGHT)):
                        mode = "pen"
                    if (x <= (2 * BUTTON_WIDTH + 3 * BUTTON_X_MARGIN) and x >= (3 * BUTTON_X_MARGIN+ BUTTON_WIDTH)) and (y >= (FLOOR + BUTTON_Y_MARGIN) and y <= (FLOOR + BUTTON_Y_MARGIN + BUTTON_HEIGHT)):
                        mode = "pencil"
                else:
                    player.go(board.find(x, y))
                player.mode(mode)
            if event.type == pygame.QUIT:
                return


if __name__ == "__main__":
    main()