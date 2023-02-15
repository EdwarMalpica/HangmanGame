import pygame

class Player:
    def __init__(self):
        #Numero de extremidades
        self.arms = 0
        # Partes del jugador
        self.playerHead = pygame.image.load("assets/img/Cabeza.png").convert()
        self.playerHead.set_colorkey([0, 0, 0])
        self.playerTorso = pygame.image.load("assets/img/Torso.png").convert()
        self.playerTorso.set_colorkey([0, 0, 0])
        self.playerRightArm = pygame.image.load("assets/img/BrazoDerecho.png").convert()
        self.playerRightArm.set_colorkey([0, 0, 0])
        self.playerLeftArm = pygame.image.load("assets/img/BrazoIzquierdo.png").convert()
        self.playerLeftArm.set_colorkey([0, 0, 0])
        self.playerLegs = pygame.image.load("assets/img/Piernas.png").convert()
        self.playerLegs.set_colorkey([0, 0, 0])
        self.soundArm = pygame.mixer.Sound("assets/sound/addArm.mp3")

    def addHead(self, screen):
        screen.blit(self.playerHead, [48, 218])

    def addTorso(self, screen):
        screen.blit(self.playerTorso, [48, 220])

    def addRightArm(self, screen):
        screen.blit(self.playerRightArm, [48, 220])

    def addLeftArm(self, screen):
        screen.blit(self.playerLeftArm, [48, 220])

    def addLegs(self, screen):
        screen.blit(self.playerLegs, [48, 220])

    def drawPlayer(self, screen):
        if self.arms == 1:
            self.addHead(screen)
        if self.arms == 2:
            self.addHead(screen)
            self.addTorso(screen)
        if self.arms == 3:
            self.addHead(screen)
            self.addTorso(screen)
            self.addLeftArm(screen)
        if self.arms == 4:
            self.addHead(screen)
            self.addTorso(screen)
            self.addLeftArm(screen)
            self.addRightArm(screen)
        if self.arms == 5:
            self.addHead(screen)
            self.addTorso(screen)
            self.addLeftArm(screen)
            self.addRightArm(screen)
            self.addLegs(screen)

    def addArm(self):
        if(self.arms<5):
            self.arms +=1
            self.soundArm.play()

