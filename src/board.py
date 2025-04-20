from squares import UnitSquare
from constants import SQUARE_SIDE
import pygame


class Board(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.start_x = x
        self.start_y = y

    def create_board(self):
#creating all the 81 squares in 9 rows and 9 columns
        self._squares = []
        start_y = self.start_y
        for _ in range (9):
            start = self.start_x
            row = []
            for _ in range(9):
                row.append(UnitSquare(start, start_y, SQUARE_SIDE ))
                start += SQUARE_SIDE
            self._squares.append(row)
            start_y += SQUARE_SIDE

    def find(self, x, y):
        