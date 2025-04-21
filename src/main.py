import pygame
from constants import *
from focus import Focus
from board import Board, draw_text
import time

def draw_pen_pencil_buttons(screen):
    pygame.draw.rect(screen, BUTTON_LINE_COLOR, BUTTON_PEN_POSITION, BUTTON_LINE_WIDTH)
    pygame.draw.rect(screen, BUTTON_LINE_COLOR, BUTTON_PENCIL_POSITION, BUTTON_LINE_WIDTH)
    pygame.draw.rect(screen, BUTTON_LINE_COLOR, BUTTON_VAL_POSITION, BUTTON_LINE_WIDTH)

def mouse_down(x, y, board, mode):
    # set selected square or change mode accordingly to where was the pressed mouse button
    if y > FLOOR:
    #tested if in board or buttons region, then test each button if in button region
        if (x <= (BUTTON_WIDTH + BUTTON_X_MARGIN) and x >= BUTTON_X_MARGIN) and (y >= (FLOOR + BUTTON_Y_MARGIN) and y <= (FLOOR + BUTTON_Y_MARGIN + BUTTON_HEIGHT)):
            mode = "pen"
            return mode
        if (x <= (2 * BUTTON_WIDTH + 3 * BUTTON_X_MARGIN) and x >= (3 * BUTTON_X_MARGIN+ BUTTON_WIDTH)) and (y >= (FLOOR + BUTTON_Y_MARGIN) and y <= (FLOOR + BUTTON_Y_MARGIN + BUTTON_HEIGHT)):
            mode = "pencil"
            return mode
        if (x <= (3 * BUTTON_WIDTH + 5 * BUTTON_X_MARGIN) and x >= (5 * BUTTON_X_MARGIN+ 2 * BUTTON_WIDTH)) and (y >= (FLOOR + BUTTON_Y_MARGIN) and y <= (FLOOR + BUTTON_Y_MARGIN + BUTTON_HEIGHT)):
            return board.validate()
    else:
        board.find(x, y)
        return None
    

def compleated(screen, status):
    if status:
        screen.fill(color="white")
        draw_text("VALID SOLUTION", pygame.font.SysFont("Arial", 60, bold=True), "green", [10,SCREEN_HEIGHT / 2], screen)
        pygame.display.flip()
        time.sleep(2)
        return False
    else:
        screen.fill(color="white", rect=FILLING_MODE_RECT)
        draw_text("invalid solution", pygame.font.SysFont("Arial", 30), "red", FILLING_MODE_XY, screen)
        return True



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    text_font = pygame.font.SysFont("Arial", 20)
    filling_mode = "pen"
    game_mode = "regular"

    focal_point = Focus()
    board = Board(BOARD_MARGIN_X, BOARD_MARGIN_Y)

    screen.fill(color="white")
    draw_pen_pencil_buttons(screen)
    draw_text(f"game mode: {game_mode}", text_font, "black", GAME_MODE_XY, screen)
    draw_text(f"filling mode: {filling_mode}", text_font, "black", FILLING_MODE_XY, screen)
    draw_text("PEN", text_font, "black", BUTTON_PEN_TEXT_POSITION, screen)
    draw_text("PENCIL", text_font, "black", BUTTON_PENCIL_TEXT_POSITION, screen)
    draw_text("VALIDATE", text_font, "black", BUTTON_VAL_TEXT_POSITION, screen)
    board.draw(screen)
    focal_point.draw(screen)

    in_game = True
    while in_game:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                # check if the mouse is pressed and where
                s = mouse_down(x, y, board, filling_mode)
                if s == True or s == False:
                    in_game = compleated(screen, s)
                elif s == "pen" or s == "pencil":
                    filling_mode = s
                    screen.fill(color="white", rect=FILLING_MODE_RECT)
                    focal_point.mode = filling_mode
                    draw_text(f"filling mode: {filling_mode}", text_font, "black", FILLING_MODE_XY, screen)
                else:
                    screen.fill(color="white", rect=focal_point.coordinates_get())
                    board.draw_square(focal_point.square_id_return(), screen)
                    focal_point.focus_go(board.squares, board.selected)
            if event.type == pygame.KEYDOWN:
                screen.fill(color="white", rect=focal_point.coordinates_get())
                board.draw_square(focal_point.square_id_return(), screen)
                key = pygame.key.get_pressed()
                focal_point.write_to_square(board.squares, key)
                focal_point.focus_go(board.squares)
                screen.fill(color="white", rect=focal_point.coordinates_get())
                board.draw_square(focal_point.square_id_return(), screen)
            if event.type == pygame.QUIT:
                return
        screen.fill(color="white", rect=focal_point.coordinates_get())
        focal_point.draw(screen)
        board.draw_square(focal_point.square_id_return(), screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()