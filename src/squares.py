import pygame

#each individual square to compose the game grid and contains the number
class UnitSquare(pygame.sprite.Sprite):
    def __init__(self, x, y, side, valor = None):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position_x = x
        self.position_y = y
        self.side = side
        self.valor = valor
        self.pencil = set()

    
    def draw(self, screen):
        return pygame.draw.rect(screen, "white", [self.position_x, self.position_y, self.side, self.side], 2)
    
    def move(self, np):
    #create a move function for the 'nonlinear' modes
        pass

    def update_pen(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_1]:
            if self.valor == 1:
                self.valor = None
            else:
                self.valor = 1
        if keys[pygame.K_2]:
            if self.valor == 2:
                self.valor = None
            else:
                self.valor = 2
        if keys[pygame.K_3]:
            if self.valor == 3:
                self.valor = None
            else:
                self.valor = 3
        if keys[pygame.K_4]:
            if self.valor == 4:
                self.valor = None
            else:
                self.valor = 4
        if keys[pygame.K_5]:
            if self.valor == 5:
                self.valor = None
            else:
                self.valor = 5
        if keys[pygame.K_6]:
            if self.valor == 6:
                self.valor = None
            else:
                self.valor = 6
        if keys[pygame.K_7]:
            if self.valor == 7:
                self.valor = None
            else:
                self.valor = 7
        if keys[pygame.K_8]:
            if self.valor == 8:
                self.valor = None
            else:
                self.valor = 8
        if keys[pygame.K_9]:
            if self.valor == 9:
                self.valor = None
            else:
                self.valor = 9

    def update_pencil(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_1]:
            if 1 in self.pencil:
                self.pencil.remove(1)
            else:
                self.pencil.add(1)
        if keys[pygame.K_2]:
            if 1 in self.pencil:
                self.pencil.remove(2)
            else:
                self.pencil.add(2)
        if keys[pygame.K_3]:
            if 1 in self.pencil:
                self.pencil.remove(3)
            else:
                self.pencil.add(3)
        if keys[pygame.K_4]:
            if 1 in self.pencil:
                self.pencil.remove(4)
            else:
                self.pencil.add(4)
        if keys[pygame.K_5]:
            if 1 in self.pencil:
                self.pencil.remove(5)
            else:
                self.pencil.add(5)
        if keys[pygame.K_6]:
            if 1 in self.pencil:
                self.pencil.remove(6)
            else:
                self.pencil.add(6)
        if keys[pygame.K_7]:
            if 1 in self.pencil:
                self.pencil.remove(7)
            else:
                self.pencil.add(7)
        if keys[pygame.K_8]:
            if 1 in self.pencil:
                self.pencil.remove(8)
            else:
                self.pencil.add(8)
        if keys[pygame.K_9]:
            if 1 in self.pencil:
                self.pencil.remove(9)
            else:
                self.pencil.add(9)