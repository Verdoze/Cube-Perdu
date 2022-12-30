from distutils import core
import pygame
from ennemi import Ennemi

#créer la classe du jeu 
class Level:
    def __init__(self,screen):
        self.screen = screen
        self.listEnnemi = []
        self.coordspwan_x = 0
        self.coordspwan_y = 0
        self.listMurV =[]
        self.listMurH=[]
        self.listMurK=[]
        
    def DrawLevel1(self):
        self.mur1 = pygame.draw.line(self.screen, 'black', [37, 210], [1043, 210], 7) #haut
        self.mur2 =pygame.draw.line(self.screen, 'black', [37, 510], [1043, 510], 7) #bas 
        self.mur3 = pygame.draw.line(self.screen, 'black', [40, 210], [40, 510], 7) #gauche
        self.mur4 = pygame.draw.line(self.screen, 'black', [1040, 210], [1040, 510], 7) #droit
        self.listMurH=[self.mur1, self.mur2]
        self.listMurV=[self.mur3, self.mur4]
        


    def DrawLevel2(self):
        self.mur1 = pygame.draw.line(self.screen, 'black', [117, 90], [963, 90], 7) #haut 
        self.mur2 = pygame.draw.line(self.screen, 'black', [117, 290], [790, 290], 7) #1er trait mid
        self.mur3 = pygame.draw.line(self.screen, 'black', [120, 87], [120, 693], 7) #gauche
        self.mur4 = pygame.draw.line(self.screen, 'black', [960, 87], [960, 693], 7) #droite
        self.mur5 = pygame.draw.line(self.screen, 'black', [288, 490], [960, 490], 7) #2eme trait mid 
        self.mur6 = pygame.draw.line(self.screen, 'black', [117, 690], [963, 690], 7) #bas 
        self.listMurV = [self.mur3, self.mur4]
        self.listMurH = [self.mur1, self.mur2, self.mur5, self.mur6]
        
        
    def DrawLevel3(self):
        self.mur1 = pygame.draw.line(self.screen, '#0b9d12', [117, 90], [963, 90], 7) #haut vert
        self.mur2 = pygame.draw.line(self.screen, '#0049b6', [120, 87], [120, 693], 7) #gauche bleu
        self.mur3 = pygame.draw.line(self.screen, '#bf0000', [960, 87], [960, 693], 7) #droit rouge
        self.mur4 = pygame.draw.line(self.screen, '#953297', [117, 690], [963, 690], 7) #bas violet
        self.mur5 = pygame.draw.line(self.screen, '#0b9d12', [117, 190], [848, 190], 7) #1er trait haut
        self.mur6 = pygame.draw.line(self.screen, '#bf0000', [847, 193], [847, 592], 7) #1er trait droit
        self.mur7 = pygame.draw.line(self.screen, '#953297', [847, 590], [234, 590], 7) #1er trait bas
        self.mur8 = pygame.draw.line(self.screen, '#0049b6', [231, 592], [231, 290], 7) #1er trait gauche
        self.mur9 = pygame.draw.line(self.screen, '#0b9d12', [235, 290], [735, 290], 7) #2eme trait haut
        self.mur10 = pygame.draw.line(self.screen, '#bf0000', [735, 289], [735, 490], 7) #2eme trait droit
        self.mur11 = pygame.draw.line(self.screen, '#953297', [735, 488], [342, 488], 7) #2eme trait bas 
        self.mur12 = pygame.draw.line(self.screen, '#0049b6', [341, 490], [341, 391], 7) #2eme trait gauche
        self.mur13 = pygame.draw.line(self.screen, '#0b9d12', [343, 390], [625, 390], 7) #3eme trait haut
        #traits sans collisions juste pour rendre le niveau plus propre
        self.mur14 = pygame.draw.line(self.screen, '#0b9d12', [848, 190], [850, 190], 7)
        self.mur15 = pygame.draw.line(self.screen, '#bf0000', [847, 592], [847, 593], 7) 
        self.mur16 = pygame.draw.line(self.screen, '#bf0000', [234, 590], [229, 590], 7)
        self.mur17 = pygame.draw.line(self.screen, '#0049b6', [231, 290], [231, 287], 7)
        self.mur18 = pygame.draw.line(self.screen, '#0b9d12', [735, 290], [735, 287], 7)
        self.mur19 = pygame.draw.line(self.screen, '#bf0000', [735, 490], [735, 491], 7)
        self.mur20 = pygame.draw.line(self.screen, '#0049b6', [338, 390], [343, 390], 7)
        self.mur21 = pygame.draw.line(self.screen, '#0049b6', [342, 488], [338, 488], 7)
        self.listMurH = [self.mur1, self.mur5, self.mur9, self.mur4, self.mur7, self.mur11, self.mur13]
        self.listMurV = [self.mur2, self.mur8, self.mur12, self.mur3, self.mur6, self.mur10]


    def DrawLevel4(self):
        self.mur1 = pygame.draw.line(self.screen, 'black',  [117, 90], [963, 90], 7) #haut 
        self.mur2 = pygame.draw.line(self.screen, 'black', [120, 87], [120, 693], 7) #gauche
        self.mur3 = pygame.draw.line(self.screen, 'black', [960, 87], [960, 693], 7) #droite
        self.mur4 = pygame.draw.line(self.screen, 'black', [117, 690], [963, 690], 7) #bas 
        self.mur5 = pygame.draw.line(self.screen, 'black', [813, 88], [813, 239], 7) #1er entrée 
        self.mur6 = pygame.draw.line(self.screen, 'black', [421, 440], [963, 440], 7) #coupe le milieu 
        self.mur7 = pygame.draw.line(self.screen, 'black', [517, 350], [813, 350], 7) #1er killer
        self.mur8 = pygame.draw.line(self.screen, 'black', [517, 240], [813, 240], 7) #au dessus de 1er killer
        self.mur9 = pygame.draw.line(self.screen, 'black', [417, 600], [417, 167], 7) #mid vertical
        self.mur10 = pygame.draw.line(self.screen, 'red', [217, 170], [537, 170], 7) #1er 1-2-3
        self.mur11 = pygame.draw.line(self.screen, 'red', [580, 170], [650, 170], 7) #2eme 1-2-3
        self.mur12 = pygame.draw.line(self.screen, 'red', [693, 170], [753, 170], 7) #3eme 1-2-3
        self.mur13 = pygame.draw.line(self.screen, 'red', [124, 270], [324, 270], 7) #gauche 1er mur
        self.mur14 = pygame.draw.line(self.screen, 'red', [230, 370], [413, 370], 7) #gauche 2eme mur
        self.mur15 = pygame.draw.line(self.screen, 'red', [124, 470], [324, 470], 7) #gauche 3eme mur
        self.mur16 = pygame.draw.line(self.screen, 'red', [230, 597], [413, 597], 7) #gauche 4eme mur
        self.mur17 = pygame.draw.line(self.screen, 'black', [483, 635], [623, 635], 7) #carre mur baS
        self.mur18 = pygame.draw.line(self.screen, 'black', [483, 635], [483, 498], 7) #carre mur gauche
        self.mur19 = pygame.draw.line(self.screen, 'red', [487, 501], [623, 501], 7) #carre mur haut
        self.mur20 = pygame.draw.line(self.screen, 'black', [623, 635], [623, 498], 7) #carre mur droit
        self.mur21 = pygame.draw.line(self.screen, 'black', [696, 635], [833, 635], 7) #carre 2 mur bas
        self.mur22 = pygame.draw.line(self.screen, 'red', [696, 638], [696, 498], 7) #carre 2 mur gauche
        self.mur23 = pygame.draw.line(self.screen, 'black', [700, 501], [833, 501], 7) #carre 2 mur haut
        self.mur24 = pygame.draw.line(self.screen, 'black', [836, 634], [836, 500], 7) #carre 2 mur droit
        self.mur25 = pygame.draw.line(self.screen, 'red', [896, 686], [896, 595], 7) #mur fin vertical bas
        self.mur26 = pygame.draw.line(self.screen, 'red', [896, 540], [896, 444], 7) #mur fin vertical haut
        self.mur27 = pygame.draw.line(self.screen, 'black', [813, 239], [813, 243], 7)
        self.mur28 = pygame.draw.line(self.screen, 'black', [517, 240], [521, 240], 7)
        self.mur29 = pygame.draw.line(self.screen, 'black', [480, 635], [483, 635], 7)
        self.mur30 = pygame.draw.line(self.screen, 'black', [623, 635], [626, 635], 7)
        self.mur31 = pygame.draw.line(self.screen, 'black', [833, 635], [839, 635], 7)
        self.mur32 = pygame.draw.line(self.screen, 'black', [836, 500], [836, 498], 7)
        self.listMurH = [self.mur1, self.mur4, self.mur6, self.mur8,self.mur17, self.mur23, self.mur21]
        self.listMurV = [self.mur2, self.mur3, self.mur5, self.mur9,self.mur18, self.mur20, self.mur24, self.mur28]
        self.listMurK = [self.mur7, self.mur10, self.mur11, self.mur12,self.mur13, self.mur14, self.mur15,self.mur16, self.mur19, self.mur22, self.mur25, self.mur26]

    def DrawEnnemiNiv1(self):
        ennemi1 = Ennemi(216, 215)
        self.listEnnemi.append(ennemi1)
        ennemi2 = Ennemi(366, 475)
        self.listEnnemi.append(ennemi2)
        ennemi3 = Ennemi(516, 215)
        self.listEnnemi.append(ennemi3)
        ennemi4 = Ennemi(666, 475)
        self.listEnnemi.append(ennemi4)
        ennemi5 = Ennemi(806, 215)
        self.listEnnemi.append(ennemi5)
        return self.listEnnemi

    def DrawEnnemiNiv2(self):        
        self.listEnnemiBas =[]
        self.listEnnemiHaut =[]
        self.listEnnemiMilieu =[]
        #ennemis en bas de gauche à droite
        ennemi1 = Ennemi(735,567)
        self.listEnnemiBas.append(ennemi1)
        ennemi2 = Ennemi(585,567)
        self.listEnnemiBas.append(ennemi2)
        ennemi3 = Ennemi(435,567)
        self.listEnnemiBas.append(ennemi3)
        ennemi4 = Ennemi(285,567)
        self.listEnnemiBas.append(ennemi4)
        #ennemis en haut  de droite à gauche
        ennemi5 = Ennemi(315,170)
        self.listEnnemiHaut.append(ennemi5)
        ennemi6 = Ennemi(465,170)
        self.listEnnemiHaut.append(ennemi6)
        ennemi7 = Ennemi(615,170)
        self.listEnnemiHaut.append(ennemi7)
        ennemi8 = Ennemi(765,170)
        self.listEnnemiHaut.append(ennemi8)
        #ennemis au milieu de droite à gauche
        ennemi9 = Ennemi(145,300)
        ennemi9.base_x = 145
        ennemi9.base_y = 300
        self.listEnnemiMilieu.append(ennemi9)    
        ennemi10 = Ennemi(345,300)
        ennemi10.base_x = 345
        ennemi10.base_y = 300
        self.listEnnemiMilieu.append(ennemi10) 
        ennemi11 = Ennemi(545,300)
        ennemi11.base_x = 545
        ennemi11.base_y = 300
        self.listEnnemiMilieu.append(ennemi11) 
        ennemi12 = Ennemi(745,300)
        ennemi12.base_x = 745
        ennemi12.base_y = 300
        self.listEnnemiMilieu.append(ennemi12)
        return (self.listEnnemiBas, self.listEnnemiHaut, self.listEnnemiMilieu)

    def DrawEnnemiNiv3(self):
        self.listEnnemiExt=[] #ennemis extérieur
        self.listEnnemiMid=[] #ennemis milieus
        self.listEnnemiInt=[] #ennemis intérieur
        ennemi1= Ennemi(160,620)
        ennemi1.base_x = 160
        ennemi1.base_y = 620
        self.listEnnemiExt.append(ennemi1)
        ennemi2= Ennemi(270,520)
        ennemi2.base_x = 270
        ennemi2.base_y = 520
        self.listEnnemiMid.append(ennemi2)
        ennemi3= Ennemi(380,430)
        ennemi3.base_x = 380
        ennemi3.base_y = 430
        self.listEnnemiInt.append(ennemi3)
        return(self.listEnnemiExt, self.listEnnemiMid, self.listEnnemiInt)
        

    def DrawEnnemiNiv4(self):
        self.listEnnemi1=[] #passage au dessus 
        self.listEnnemi2=[] #passage en dessous
        self.listEnnemi3=[] #en haut
        self.listEnnemi4=[] #grande ligne sur la gauche
        self.listEnnemi5=[] #autour des carrés
        ennemi1 = Ennemi(630,280)
        self.listEnnemi1.append(ennemi1)
        ennemi2 =Ennemi(635, 370)
        self.listEnnemi2.append(ennemi2)
        ennemi3 = Ennemi(635,390)
        self.listEnnemi2.append(ennemi3)
        ennemi4 =Ennemi(150, 120)
        self.listEnnemi3.append(ennemi4)
        ennemi5 =Ennemi(320, 620)
        self.listEnnemi3.append(ennemi5)
        return(self.listEnnemi1, self.listEnnemi2, self.listEnnemi3)
        
            
