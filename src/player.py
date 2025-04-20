import pygame

#a way to show where you are writing and keep track of things
class Player(pygame.sprite.Sprite):
    def __init__(self):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

    # in the player class
    def coordinates(self, square):
        a = self.position_x 
        b = self.position_y

        return [a, b, c, d]
    
    def draw(self, screen):
        return pygame.draw.rect(screen, "white", self.coordinates(), 2)