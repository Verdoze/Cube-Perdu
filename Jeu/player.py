import pygame

#créer la classe du joueur
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.health = 1
        self.max_health = 1
        self.velocity = [0,0]
        self.speed = 5
        self.image = pygame.image.load('images/carré.png') 
        self.rect = self.rect = pygame.Rect(x,y ,32,32)


    def move(self):
        self.rect.move_ip(self.velocity[0]*self.speed, self.velocity[1]*self.speed)

    def spawnLvl1(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def spawnLvl2(self, x, y):
        self.rect.x = 890
        self.rect.y = 575

    def spawnLvl3(self):
        self.rect.x = 160
        self.rect.y = 125