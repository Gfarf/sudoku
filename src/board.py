from squares import UnitSquare
from constants import *
import pygame
from logic import *


pygame.font.init()
def draw_text(text, font, font_color, position, screen):
    img = font.render(text, True, font_color)
    screen.blit(img, position)

class Board(pygame.sprite.Sprite):
    PEN_FONT = pygame.font.SysFont("Arial", PEN_HEIGHT)
    PENCIL_FONT = pygame.font.SysFont("Arial", PENCIL_HEIGTH)
    def __init__(self, x, y):
        super().__init__()
        self.start_x = x
        self.start_y = y
        self.create_board()
        self.selected = (0,0)

    def create_board(self):
#creating all the 81 squares in 9 rows and 9 columns
        self.squares = []
        board = create_new_board()
        start_y = self.start_y
        for i in range (9):
            start = self.start_x
            row = []
            for j in range(9):
                row.append(UnitSquare(start, start_y, SQUARE_SIDE ))
                row[j].true_valor = board[i][j]
                start += SQUARE_SIDE
            self.squares.append(row)
            start_y += SQUARE_SIDE

    def draw(self, screen):
#drawing the outer layer and groups, will need to refactor to make the schizo modes work, but should be enough for regular and moving
        for i in range(9):
            for j in range(9):
                self.squares[i][j].draw(screen)
        pygame.draw.rect(screen, "black", [self.start_x, self.start_y, SQUARE_SIDE * 9, SQUARE_SIDE * 9], OUTER_THICK)

    def render_board(self):
        board = []
        for i in range(9):
            row = []
            for j in range(9):
                if self.squares[i][j].true_valor is not None:
                    row.append(self.squares[i][j].true_valor)
                else:
                    row.append(self.squares[i][j].valor)
            board.append(row)
        return board
    
    def validate(self):
        return validating_board(self.render_board())

    def draw_square(self, square_id, screen):
        self.squares[square_id[0]][square_id[1]].draw(screen)

    def find(self, x, y):
        for i in range(9):
            for j in range(9):
                if self.squares[i][j].inside_the_square(x, y):
                    self.selected = (i, j)
                    return 
