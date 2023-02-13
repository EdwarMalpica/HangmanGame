import pygame, sys

from view.Player import Player

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class MainView:
    def __init__(self):
        self.game = pygame.init()
        self.screen = pygame.display.set_mode((700,512))
        self.clock = pygame.time.Clock()
        self.player = Player()
        self.game_over = False
        self.background = pygame.image.load("assets/img/FondoJuego.png").convert()
        self.sounBack = pygame.mixer.Sound("assets/sound/Back.mp3")


    def mainLoop(self):
        self.sounBack.play()
        while not self.game_over:
            self.eventsControl()
            self.initComponents()
            print(pygame.mouse.get_pos())
        pygame.quit()

    def eventsControl(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.player.addArm()

    def initComponents(self):
        self.screen.blit(self.background, [0, 0])
        self.player.drawPlayer(self.screen)
        pygame.display.flip()
        self.clock.tick(30)



mainVies = MainView()
mainVies.mainLoop()

