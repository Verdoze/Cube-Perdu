import pygame
from player import Player
from level import Level

#créer la classe du jeu 
class Game:
    def __init__(self, screen):
        #definir si le jeu a commencé ou pas 
        self.is_playing = False
        self.pressed = {}
        self.appuie = False
        self.screen = screen
        self.level = Level(screen)
        #generer les ennemis
        self.listEnnemi =[]
             
        self.all_ennemis = pygame.sprite.Group()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            gauche = True
            if gauche == True:
                self.player.velocity[0] = -1
                for item in self.level.listMurV:
                    if self.player.rect.colliderect(item) and self.player.rect[2] > item[2] and self.player.rect[0] > item[0]:
                        gauche = False
                        if self.player.rect.colliderect(item):
                            self.player.velocity[0] = 0
        elif keys[pygame.K_RIGHT]:
            droit = True
            if droit == True:
                self.player.velocity[0] = 1
                for item in self.level.listMurV:
                    if self.player.rect.colliderect(item) and self.player.rect[0] < item[0]:
                        droit = False
                        if self.player.rect.colliderect(item):
                            self.player.velocity[0] = 0
        else:
            self.player.velocity[0] = 0
        if keys[pygame.K_UP]:
            haut = True
            if haut == True:
                self.player.velocity[1] = -1
                for item in self.level.listMurH:
                    if self.player.rect.colliderect(item) and self.player.rect[1] > item[1] and self.player.rect[2] < item[2]:
                        haut = False
                        if self.player.rect.colliderect(item):
                            self.player.velocity[1] = 0
        elif keys[pygame.K_DOWN]:
            bas = True
            if bas == True:
                self.player.velocity[1] = 1
                for item in self.level.listMurH:
                    if self.player.rect.colliderect(item) and self.player.rect[1] < item[1]:
                        bas = False
                        if self.player.rect.colliderect(item):
                            self.player.velocity[1] = 0
        else:
            self.player.velocity[1] = 0


    def update(self, screen):
        screen.blit(self.player.image, self.player.rect)
        self.player.move()
        
        #si tu fermes la fenêtre 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    def setNiv1(self, screen, fond1 ,play_fond1, x, y):
        self.level = Level(screen)
        self.level.DrawLevel1()
        self.level.DrawEnnemiNiv1()
        self.player = Player(x, y)
        return self.level
    
    def updateElementsNiv1(self,screen):
        self.level.DrawLevel1()
        for ennemiLvl1 in self.level.listEnnemi:
            screen.blit(ennemiLvl1.image,(ennemiLvl1.rect.x, ennemiLvl1.rect.y))
            

    def setNiv2(self, screen, fond2,play_fond2,x, y):
        self.level = Level(screen)
        screen.blit(fond2, play_fond2)        
        self.level.DrawLevel2()
        self.level.DrawEnnemiNiv2()       
        self.player = Player(x, y)        
        return self.level
    
    def updateElementsNiv2(self,screen,ligne_arr2, ligne_arr_rectNiv2):
        screen.blit(ligne_arr2, ligne_arr_rectNiv2)
        self.level.DrawLevel2()                 
        for i in range (len(self.level.listEnnemiHaut)):
            screen.blit(self.level.listEnnemiHaut[i].image,(self.level.listEnnemiHaut[i].rect.x, self.level.listEnnemiHaut[i].rect.y))
            screen.blit(self.level.listEnnemiBas[i].image,(self.level.listEnnemiBas[i].rect.x, self.level.listEnnemiBas[i].rect.y))
            screen.blit(self.level.listEnnemiMilieu[i].image,(self.level.listEnnemiMilieu[i].rect.x, self.level.listEnnemiMilieu[i].rect.y))
            

        
    def setNiv3(self, screen, image_damier3,play_image_damier3, x, y):
        self.level = Level(screen)
        self.player = Player(x, y)
        screen.blit(image_damier3, play_image_damier3)
        self.level.DrawLevel3()
        self.level.DrawEnnemiNiv3()
        return self.level
    
    def updateElementsNiv3(self,screen):
        self.level.DrawLevel3()
        for i in range(len(self.level.listEnnemiExt)):
            screen.blit(self.level.listEnnemiExt[i].image,(self.level.listEnnemiExt[i].rect.x, self.level.listEnnemiExt[i].rect.y))
            screen.blit(self.level.listEnnemiMid[i].image,(self.level.listEnnemiMid[i].rect.x, self.level.listEnnemiMid[i].rect.y))
            screen.blit(self.level.listEnnemiInt[i].image,(self.level.listEnnemiInt[i].rect.x, self.level.listEnnemiInt[i].rect.y))


    def setNiv4(self, screen, image_damier4,play_image_damier4, x, y):
        self.level = Level(screen)
        self.player = Player(x, y)
        screen.blit(image_damier4, play_image_damier4)
        self.level.DrawLevel4()
        self.level.DrawEnnemiNiv4()
        return self.level

    def updateElementsNiv4(self,screen):
        self.level.DrawLevel4()
        for i in range (len(self.level.listEnnemi1)):
            screen.blit(self.level.listEnnemi1[i].image,(self.level.listEnnemi1[i].rect.x, self.level.listEnnemi1[i].rect.y))

        for i in range (len(self.level.listEnnemi2)):
            screen.blit(self.level.listEnnemi2[i].image,(self.level.listEnnemi2[i].rect.x, self.level.listEnnemi2[i].rect.y))
            screen.blit(self.level.listEnnemi3[i].image,(self.level.listEnnemi3[i].rect.x, self.level.listEnnemi3[i].rect.y))   
        
