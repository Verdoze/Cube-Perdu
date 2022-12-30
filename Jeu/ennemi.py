from mimetypes import init
import pygame

class Ennemi(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.velocity = 5
        self.image = pygame.image.load('images/ennemi.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.size = 30
        self.sens = ""
        self.base_x= 0
        self.base_y =0 


    def move_up(self):
        self.rect.y -= self.velocity
    def move_down(self):
        self.rect.y += self.velocity
    def move_right(self):
        self.rect.x += self.velocity
    def move_left(self):
        self.rect.x -= self.velocity
        
    