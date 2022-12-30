from json.tool import main
from pickle import FALSE
from tkinter import Button
import pygame
from game import Game
from level import Level
from ennemi import Ennemi

pygame.init()

#Création de la fenêtre de jeu 
pygame.display.set_caption("Carré perdu")
screen = pygame.display.set_mode((1080, 720))

#charger les images dans le jeu (elles sont non voyantes après ça)
background = pygame.image.load('images/bck6.jpg')
banner = pygame.image.load('images/banniere.png')
play_button = pygame.image.load('images/button.png')
bouton_retour = pygame.image.load('images/retour.png')
bouton_mort = pygame.image.load('images/mort.png')
fond1 = pygame.image.load('images/fond1.jpg')
fond2 = pygame.image.load('images/fond2.jpg')
fond3 = pygame.image.load('images/fond3.jpg')
fond4 = pygame.image.load('images/fond4.jpg')
ligne_arr = pygame.image.load('images/lignearr.png')
ligne_arr2 =pygame.image.load('images/lignearr2.png')
ligne_arr3 = pygame.image.load('images/lignearr3.png')
ligne_arr4 = pygame.image.load('images/lignearr4.png')
level1_button = pygame.image.load('images/level1.png')
level2_button = pygame.image.load('images/level2.png')
level3_button = pygame.image.load('images/level3.png')
level4_button = pygame.image.load('images/level4.png')

#attribuer un rect aux images
banner_rect = banner.get_rect()
play_button_rect = play_button.get_rect()
play_retour_bouton = bouton_retour.get_rect()
play_bouton_mort = bouton_mort.get_rect()
play_fond1 = fond1.get_rect()
play_fond2 = fond2.get_rect()
play_fond3 = fond3.get_rect()
play_fond4 = fond4.get_rect()
level1_button_rect = level1_button.get_rect()
level2_button_rect = level2_button.get_rect()
level3_button_rect = level3_button.get_rect()
level4_button_rect = level4_button.get_rect()
ligne_arr_rectNiv1= ligne_arr.get_rect()
ligne_arr_rectNiv2 =ligne_arr2.get_rect()
ligne_arr_rectNiv3= ligne_arr3.get_rect()
ligne_arr_rectNiv4= ligne_arr4.get_rect()


#attribuer une position aux images
play_button_rect.x = 390
play_button_rect.y = 420
play_retour_bouton.x = 10
play_retour_bouton.y = 10
play_bouton_mort.x = 875
play_bouton_mort.y = 10
play_fond1.x = 40
play_fond1.y = 210
play_fond2.x = 120
play_fond2.y = 90
play_fond3.x = 120
play_fond3.y = 90
play_fond4.x = 120
play_fond4.y = 90 
#ligne dep et arr niv1
ligne_arr_rectNiv1.x = 988
ligne_arr_rectNiv1.y = 210
#ligne dep et arr niv2
ligne_arr_rectNiv2.x = 117
ligne_arr_rectNiv2.y = 87

#ligne arr niv3
ligne_arr_rectNiv3.x = 341
ligne_arr_rectNiv3.y = 395
#ligne arr niv4
ligne_arr_rectNiv4.x = 896
ligne_arr_rectNiv4.y = 444

#boutons de sélection de niveau du menu
level1_button_rect.x = 80
level1_button_rect.y = 365
level2_button_rect.x = 80
level2_button_rect.y = 510
level3_button_rect.x = 770
level3_button_rect.y = 365
level4_button_rect.x = 770
level4_button_rect.y = 510

#compteur de mort
myFont = pygame.font.SysFont("Arial", 35) #police d'ecriture
compteurMorts = 0
lvl = 0 
incr=0

#charger notre jeu
game = Game(screen)
running = True
imgdamier =True    

while running:
    #mettre les images sur le jeu
    screen.blit(background,(0,0))
    
    #gere les events
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                   
            #clic sur play lance après le menu
            elif event.type == pygame.MOUSEBUTTONDOWN :
                if play_button_rect.collidepoint(event.pos) and lvl== 0:                    
                    lvl = 1
                    level1 = game.setNiv1(screen, fond1, play_fond1, 55, 345) 
                    game.is_playing = True
                if level1_button_rect.collidepoint(event.pos) and lvl== 0:                     
                    lvl = 1
                    level1 = game.setNiv1(screen, fond1, play_fond1, 55, 345) 
                    game.is_playing = True

                if level2_button_rect.collidepoint(event.pos) and lvl== 0:                    
                    lvl = 2
                    level2 = game.setNiv2(screen, fond2,play_fond2, 890, 575)
                    game.is_playing = True   

                if level3_button_rect.collidepoint(event.pos) and lvl== 0:                     
                    lvl = 3
                    level3 = game.setNiv3(screen, fond3, play_fond3, 160, 125) 
                    game.is_playing = True 
                if level4_button_rect.collidepoint(event.pos) and lvl== 0:
                    lvl = 4
                    level4 = game.setNiv4(screen, fond4, play_fond4, 870, 120) 
                    game.is_playing = True

                if play_retour_bouton.collidepoint(event.pos):
                    game.is_playing = False
                    compteurMorts = 0
                    lvl=0
                    incr = 0
         
    #le jeu se lance après appuie sur play et affiche les "evenements" suivant le niveau choisi
    if game.is_playing:
        game.events()    
        screen.blit(bouton_retour, play_retour_bouton)
        screen.blit(bouton_mort, play_bouton_mort)
        affichageMort = myFont.render(str(compteurMorts), True,(0,0,0))
        screen.blit(affichageMort,(977,22))

        if lvl==1 :
            screen.blit(fond1, play_fond1)
            game.update(screen)  #update du Joueur
            game.updateElementsNiv1(screen)
            if incr == 0 :
                i=0
                incr += 1
                for item in level1.listEnnemi :#boucle qui va attribuer le sens de déplacement des ennemis du niveau 1 en alternant                     
                    if i == 0 :
                        item.sens = "descend"
                        i == 1
                    elif i == 1:
                        item.sens ="monte"
                        i = 0
            for item in level1.listEnnemi:#boucle de déplacements des ennemis pour le niveau 1
                if item.rect.y > 210 and item.sens == "monte":
                    item.move_up()
                    if item.rect.y <= 210:
                        item.sens = "descend"
                elif (item.rect.y < 510 - item.size and item.sens == "descend"):
                    item.move_down()
                    if item.rect.y >= 510 - item.size:
                        item.sens = "monte"                                 
       
                if item.rect.colliderect(game.player.rect):#collision entre le joueur et les ennemis
                    compteurMorts += 1
                    game.player.rect.x = 75 
                    game.player.rect.y = 350
                
            if game.player.rect.colliderect(ligne_arr_rectNiv1): #lorsque le joueur touche la ligne d'arrivée passe au niveau suivant              
                lvl = 2 
                incr = 0               
                screen.fill((0,0,0))  
                game.is_playing = True
                level2 = game.setNiv2(screen, fond2,play_fond2, 890, 575)

        #instructions du niveau 2
        if lvl == 2 :
            screen.blit(fond2, play_fond2)
            screen.blit(ligne_arr2, ligne_arr_rectNiv2)  
            game.update(screen)  #update du Joueur                       
            game.updateElementsNiv2(screen, ligne_arr2, ligne_arr_rectNiv2) #update des éléments (niveau, ennemis)
            
            if incr == 0 :
                incr += 1
                i = 0
                for item in level2.listEnnemiHaut :#boucle qui va attribuer le sens de déplacement des ennemis du niveau 1 en alternant
                        if i == 0 :
                            item.sens = "monte"
                            i = 1
                        elif i == 1:
                            item.sens ="descend"
                            i = 0
                for item in level2.listEnnemiBas :#boucle qui va attribuer le sens de déplacement des ennemis du niveau 1 en alternant 
                        if i == 0 :
                            item.sens = "descend"
                            i = 1
                        elif i == 1:
                            item.sens ="monte"
                            i = 0
            #boucle de déplacements des ennemis  du haut pour le niveau 2            
            for item in level2.listEnnemiHaut:
                if item.rect.y > 90 and item.sens == "monte":
                    item.move_up()
                    if item.rect.y <= 90:
                        item.sens = "descend"                    
                elif (item.rect.y < 285 - item.size and item.sens == "descend"):
                    item.move_down()
                    if item.rect.y >= 285 - item.size:
                        item.sens = "monte"
                if item.rect.colliderect(game.player.rect):#collision entre le joueur et les ennemis
                    compteurMorts += 1
                    game.player.rect.x = 890 
                    game.player.rect.y = 575
            #boucle de déplacements des ennemis du bas pour le niveau 2
            for item in level2.listEnnemiBas:
                if item.rect.y > 490 and item.sens == "monte":
                    item.move_up()
                    if item.rect.y <= 490:
                        item.sens = "descend"
                elif (item.rect.y < 690 - item.size and item.sens == "descend"):
                    item.move_down()
                    if item.rect.y >= 690 - item.size:
                        item.sens = "monte"
                if item.rect.colliderect(game.player.rect):#collision entre le joueur et les ennemis
                    compteurMorts += 1
                    game.player.rect.x = 890 
                    game.player.rect.y = 575
            #boucle de déplacements des ennemis au millieu pour le niveau 2
            for item in level2.listEnnemiMilieu:
                if  item.rect.x < (item.base_x +150) and item.rect.y == 300 :#vérfie que l'ennemi soit en haut a gauche
                    item.move_right()                    
                if  item.rect.x == (item.base_x +150) and item.rect.y >= 300 :#vérfie que l'ennemi soit en haut a droite
                    item.move_down()
                if  item.rect.x > (item.base_x ) and item.rect.y == (item.base_y + 150):#vérfie que l'ennemi soit en bas a droite
                    item.move_left()  
                if  item.rect.x == (item.base_x) and  item.rect.y <= (item.base_y +150):#vérfie que l'ennemi soit en bas a gauche
                    item.move_up()
                if item.rect.colliderect(game.player.rect):#collision entre le joueur et les ennemis
                    compteurMorts += 1
                    game.player.rect.x = 890 
                    game.player.rect.y = 575
            if game.player.rect.colliderect(ligne_arr_rectNiv2): #lorsque le joueur touche la ligne d'arrivée passe au niveau suivant              
                    lvl = 3
                    incr = 0               
                    screen.fill((0,0,0))  
                    game.is_playing = True
                    level3 = game.setNiv3(screen, fond3, play_fond3, 160, 125)  #instancie le niveau3           

        if lvl == 3 :
            screen.blit(fond3, play_fond3)#update du fond
            game.update(screen)  #update du Joueur
            game.updateElementsNiv3(screen)

            for item in level3.listEnnemiExt:#déplacement pour l'ennemi à l'extérieur
                if  item.rect.x == (item.base_x) and  item.rect.y <= (item.base_y):#vérfie que l'ennemi soit en bas a gauche
                    item.move_up()
                if  item.rect.x <= (item.base_x +750- item.size/2) and item.rect.y == (item.base_y - 500) :#vérfie que l'ennemi soit en haut a gauche
                    item.move_right()                              
                if  item.rect.x == (item.base_x + 750-item.size/2) and item.rect.y <= (item.base_y ) :#vérfie que l'ennemi soit en haut a droite
                    item.move_down()                    
                if  item.rect.x <= (item.base_x + 750-item.size/2) and item.rect.y ==(item.base_y):#vérfie que l'ennemi soit en bas a droite
                    item.move_left()
                if item.rect.colliderect(game.player.rect):#collision entre le joueur et les ennemis
                    compteurMorts += 1
                    game.player.rect.x = 160 
                    game.player.rect.y = 125

            for item in level3.listEnnemiMid:#déplacement pour l'ennemi au milieur
                if  item.rect.x == (item.base_x) and  item.rect.y <= (item.base_y):#vérfie que l'ennemi soit en bas a gauche
                    item.move_up()
                if  item.rect.x <= (item.base_x + 520 -item.size/2) and item.rect.y == (item.base_y - 300) :#vérfie que l'ennemi soit en haut a gauche
                    item.move_right()                              
                if  item.rect.x == (item.base_x + 520-item.size/2) and item.rect.y <= (item.base_y ) :#vérfie que l'ennemi soit en haut a droite
                    item.move_down()                    
                if  item.rect.x <= (item.base_x + 520-item.size/2) and item.rect.y ==(item.base_y):#vérfie que l'ennemi soit en bas a droite
                    item.move_left()
                if item.rect.colliderect(game.player.rect):#collision entre le joueur et les ennemis
                    compteurMorts += 1
                    game.player.rect.x = 160 
                    game.player.rect.y = 125
                                
            for item in level3.listEnnemiInt:#déplacement pour l'ennemi à l'intérieur
                if  item.rect.x == (item.base_x) and  item.rect.y <= (item.base_y):#vérfie que l'ennemi soit en bas a gauche
                    item.move_up()
                if  item.rect.x <= (item.base_x +300 -item.size/2) and item.rect.y == (item.base_y - 100) :#vérfie que l'ennemi soit en haut a gauche
                    item.move_right()                              
                if  item.rect.x == (item.base_x + 300-item.size/2) and item.rect.y <= (item.base_y ) :#vérfie que l'ennemi soit en haut a droite
                    item.move_down()                    
                if  item.rect.x <= (item.base_x + 300-item.size/2) and item.rect.y ==(item.base_y):#vérfie que l'ennemi soit en bas a droite
                    item.move_left()
                if item.rect.colliderect(game.player.rect):#collision entre le joueur et les ennemis
                    compteurMorts += 1
                    game.player.rect.x = 160 
                    game.player.rect.y = 125

            if game.player.rect.colliderect(ligne_arr_rectNiv3):
                    lvl = 4
                    incr = 0
                    screen.fill((0,0,0)) 
                    game.is_playing = True
                    level4 = game.setNiv4(screen, fond4, play_fond3,  870, 120)
        if lvl == 4:
            screen.blit(fond4, play_fond4)#update du fond
            game.update(screen)  #update du Joueur  
            game.updateElementsNiv4(screen)
            i=0
            for item in game.level.listEnnemi1:
                if i == 0 :
                    item.sens = "descend"
                    i = 1
                elif i == 1:
                    item.sens ="monte"
                    i = 0
            for item in game.level.listEnnemi2:
                if i == 0 :
                    item.sens = "descend"
                    i = 1
                elif i == 1:
                    item.sens ="monte"
                    i = 0
                                          
            for item in game.level.listMurK:#si le joueur touche un mur rouge il recommence
                    if game.player.rect.colliderect(item):
                        compteurMorts += 1
                        game.player.rect.x = 870
                        game.player.rect.y = 120  

            for item in level4.listEnnemi1:#boucle de déplacements des ennemis pour le niveau 4
                if item.rect.y <350  and item.sens == "monte":
                    item.move_up()
                    if item.rect.y <= 240 :
                        item.sens = "descend"                
                if item.rect.y <= 350 and item.sens == "descend":
                    item.move_down()
                    if item.rect.y >= 350:
                        item.sens= "monte"            
                    print (item.rect.y, item.rect.y-item.size, item.sens, item.size)
            
            for item in level4.listEnnemi2:
                if item.rect.x > 417 and item.sens == "monte":
                    item.move_right()
                    if item.rect.x >= 960 :
                        item.sens="descend"
                if item.rect.x < 960 and item.sens =="descend":
                    item.move_left()
                    if item.rect.x <= 417:
                        item.sens="monte"





            if game.player.rect.colliderect(ligne_arr_rectNiv4):
                    lvl = 0
                    game.is_playing = False
                    print("bien joué ma moula!")

    else:
        screen.blit(banner, (180, 90))
        screen.blit(play_button, play_button_rect)
        screen.blit(level1_button, level1_button_rect)
        screen.blit(level2_button, level2_button_rect)
        screen.blit(level3_button, level3_button_rect)
        screen.blit(level4_button, level4_button_rect)    

 
        

    #mise à jour de l'écran fps
    clock = pygame.time.Clock()
    clock.tick(90)
    pygame.display.flip()