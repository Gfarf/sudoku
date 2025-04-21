import pygame
from constants import *
from squares import UnitSquare

#a way to show where you are writing and keep track of things
class Focus(pygame.sprite.Sprite):
    def __init__(self):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.mode = "pen"
        self.i = 0
        self.j = 0
        self.coordinates = [BOARD_MARGIN_X, BOARD_MARGIN_Y, SQUARE_SIDE, SQUARE_SIDE]
    
        

    # in the player class
    def coordinates_set(self, square_list):
        a = square_list[self.i][self.j].position_x 
        b = square_list[self.i][self.j].position_y
        c = SQUARE_SIDE
        d = SQUARE_SIDE
        self.coordinates = [a, b, c, d]

    def coordinates_get(self):
        return self.coordinates
    
    def draw(self, screen):
        return pygame.draw.rect(screen, "yellow", self.coordinates, FOCUS_THICK)
    
    def focus_go(self, square_list, indexes=None):
        if indexes is not None:
            self.i = indexes[0]
            self.j = indexes[1]
        self.coordinates_set(square_list)

    def square_id_return(self):
        return (self.i, self.j)
    
    def move_with_key(self, keys):
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            if self.j == 0:
                self.j = 9
            self.j -= 1
            return 
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            if self.j == 8:
                self.j = -1
            self.j += 1
            return True
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            if self.i == 8:
                self.i = -1
            self.i += 1
            return True
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            if self.i == 0:
                self.i = 9
            self.i -= 1
            return True
        return False


    def write_to_square(self, square_list, event):
        keys = event
        if self.move_with_key(keys):
            return
        square = square_list[self.i][self.j]
        if keys[pygame.K_DELETE]:
            square.pencil.clear()
            square.valor = None
            return
        if self.mode == "pencil":
            if keys[pygame.K_1] or keys[pygame.K_KP1]:
                if 1 in square.pencil:
                    square.pencil.remove(1)
                else:
                    square.pencil.add(1)
            if keys[pygame.K_2] or keys[pygame.K_KP2]:
                if 2 in square.pencil:
                    square.pencil.remove(2)
                else:
                    square.pencil.add(2)
            if keys[pygame.K_3] or keys[pygame.K_KP3]:
                if 3 in square.pencil:
                    square.pencil.remove(3)
                else:
                    square.pencil.add(3)
            if keys[pygame.K_4] or keys[pygame.K_KP4]:
                if 4 in square.pencil:
                    square.pencil.remove(4)
                else:
                    square.pencil.add(4)
            if keys[pygame.K_5] or keys[pygame.K_KP5]:
                if 5 in square.pencil:
                    square.pencil.remove(5)
                else:
                    square.pencil.add(5)
            if keys[pygame.K_6] or keys[pygame.K_KP6]:
                if 6 in square.pencil:
                    square.pencil.remove(6)
                else:
                    square.pencil.add(6)
            if keys[pygame.K_7] or keys[pygame.K_KP7]:
                if 7 in square.pencil:
                    square.pencil.remove(7)
                else:
                    square.pencil.add(7)
            if keys[pygame.K_8] or keys[pygame.K_KP8]:
                if 8 in square.pencil:
                    square.pencil.remove(8)
                else:
                    square.pencil.add(8)
            if keys[pygame.K_9] or keys[pygame.K_KP9]:
                if 9 in square.pencil:
                    square.pencil.remove(9)
                else:
                    square.pencil.add(9)
        if self.mode == "pen":
            if keys[pygame.K_1] or keys[pygame.K_KP1]:
                if square.valor == 1:
                    square.valor = None
                else:
                    square.valor = 1
            if keys[pygame.K_2] or keys[pygame.K_KP2]:
                if square.valor == 2:
                    square.valor = None
                else:
                    square.valor = 2
            if keys[pygame.K_3] or keys[pygame.K_KP3]:
                if square.valor == 3:
                    square.valor = None
                else:
                    square.valor = 3
            if keys[pygame.K_4] or keys[pygame.K_KP4]:
                if square.valor == 4:
                    square.valor = None
                else:
                    square.valor = 4
            if keys[pygame.K_5] or keys[pygame.K_KP5]:
                if square.valor == 5:
                    square.valor = None
                else:
                    square.valor = 5
            if keys[pygame.K_6] or keys[pygame.K_KP6]:
                if square.valor == 6:
                    square.valor = None
                else:
                    square.valor = 6
            if keys[pygame.K_7] or keys[pygame.K_KP7]:
                if square.valor == 7:
                    square.valor = None
                else:
                    square.valor = 7
            if keys[pygame.K_8] or keys[pygame.K_KP8]:
                if square.valor == 8:
                    square.valor = None
                else:
                    square.valor = 8
            if keys[pygame.K_9] or keys[pygame.K_KP9]:
                if square.valor == 9:
                    square.valor = None
                else:
                    square.valor = 9