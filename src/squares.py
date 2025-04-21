import pygame
from constants import *

pygame.font.init()
def draw_text(text, font, font_color, position, screen):
    img = font.render(text, True, font_color)
    screen.blit(img, position)

#each individual square to compose the game grid and contains the number
class UnitSquare(pygame.sprite.Sprite):
    def __init__(self, x, y, side, valor = None, true_valor = None):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position_x = x
        self.position_y = y
        self.side = side
        self.valor = valor
        self.pencil = set()
        self.true_valor = true_valor

    
    def draw(self, screen):
        pygame.draw.rect(screen, "black", [self.position_x, self.position_y, self.side, self.side], INNER_THICK)
        pos = (self.position_x + self.side/3, self.position_y + self.side/4)
        if self.true_valor is not None:
            draw_text(f"{self.true_valor}", pygame.font.SysFont("Arial", PEN_HEIGHT), "black", pos, screen)
        elif self.valor is not None:
            draw_text(f"{self.valor}", pygame.font.SysFont("Arial", PEN_HEIGHT), "blue", pos, screen)
        else:
            x1 = self.position_x + PENCIL_MARGIN
            y1 = self.position_y + PENCIL_MARGIN
            for n in sorted(self.pencil):
                draw_text(f"{n}", pygame.font.SysFont("Arial", PENCIL_HEIGTH), "black", (x1, y1), screen)
                x1 += PENCIL_MARGIN

    
    def move(self, np):
    #create a move function for the 'nonlinear' modes
        pass

    def inside_the_square(self, x, y):
        if x >= self.position_x and x <= self.position_x + self.side:
            if y >= self.position_y and y <= self.position_y + self.side:
                return True
        return False
