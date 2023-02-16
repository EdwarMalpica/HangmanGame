import pygame, sys

from view.Player import Player
from view.Button import Button

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


class MainView:

    """
    game: inicializa Pygame.
    screen: establece el tamaño de la ventana del juego en 700x512 píxeles.
    clock: controla la tasa de refresco del juego.
    player: un objeto de la clase Player que se utiliza para dibujar el jugador.
    game_over: una bandera que indica si el juego ha terminado.
    background: la imagen de fondo que se muestra en la ventana del juego.
    sounBack: el sonido de fondo que se reproducirá mientras el juego esté en curso.
    """
    def resetView(self):

        #Estados del juego
        self.game_over = False
        self.game_pause = False
        self.menu_state = "main"
        self.player = Player()
        self.game_win = False
        self.game_quit = False
        self.get_data_length = False
        self.check_char = False
        self.isCorrect = False
        self.isResponse = False
        self.checUserName = False

        self.userText = ""
        self.startTime = 0
        self.lenWord = 0
        self.check = {}
        self.lives = 0
        self.backWord = ''
        self.totalTime = 0
        self.totalScore = 0
        self.resetWin = False


    def __init__(self):

        self.game = pygame.init()
        self.screen = pygame.display.set_mode((700,512))
        self.caption = pygame.display.set_caption("HangMan")
        self.clock = pygame.time.Clock()
        self.player = Player()
        #Estados del juego
        self.game_over = False
        self.game_pause = False
        self.menu_state = "main"
        self.game_win = False
        self.game_quit = False
        self.get_data_length = False
        self.check_char = False
        self.isCorrect = False
        self.isResponse = False
        self.checUserName = False
        self.resetWin = False

        self.background = pygame.image.load("assets/img/FondoJuego.png").convert()
        self.sounBack = pygame.mixer.Sound("assets/sound/Back.mp3")
        self.soundIncorrect = pygame.mixer.Sound("assets/sound/incorrect.mp3")
        self.soundCorrect = pygame.mixer.Sound("assets/sound/correct.mp3")
        self.font = pygame.font.SysFont("arialBlack", 30)
        self.userText = ""
        self.startTime = 0
        self.lenWord = 0
        self.check = {}
        self.lives = 0
        self.loadImagesMenu()
        self.totalTime = 0
        self.totalScore = 0


    def getState(self):
        return self.game_pause


    def startGame(self):
        self.get_data_length = True

        #self.check = [0] * len(self.word)



    def drawBaseWord(self):
        for i in range(0, self.lenWord):
            self.screen.blit(self.imgBaseWord, [200 + (i*55),200])


    def drawWordOnBase(self):

        for clave, valor in self.check.items():
            text = self.font.render(valor, True, RED)
            self.screen.blit(text,[220 +(clave*55), 180])


    def loadImagesMenu(self):
        self.imgJugar = pygame.image.load("assets/img/buttonJugar.png").convert_alpha()
        self.imgRanking = pygame.image.load("assets/img/buttonRanking.png").convert_alpha()
        self.imgSalir = pygame.image.load("assets/img/buttonSalir.png").convert_alpha()
        self.imgReanudar = pygame.image.load("assets/img/buttonReanudar.png").convert_alpha()
        self.imgBaseWord = pygame.image.load("assets/img/baseWord.png").convert_alpha()
        self.imgInputText = pygame.image.load("assets/img/inputText.png").convert_alpha()
        self.imgMainMenu = pygame.image.load("assets/img/FondoMenu.png").convert()
        self.imgBackPause = pygame.image.load("assets/img/FondoPausa.png").convert()
        self.imgTitleMain = pygame.image.load("assets/img/HANGMAN.png")
        self.imgGameOver =  pygame.image.load("assets/img/gameOver.png").convert()
        self.imgWin = pygame.image.load("assets/img/win.png").convert()
        self.imgRankingBack = pygame.image.load("assets/img/reanking.png")

        self.buttonJugar = Button(300, 180, self.imgJugar, 1)
        self.buttonRanking = Button(300, 250, self.imgRanking, 1)
        self.buttonSalir = Button(300, 320, self.imgSalir, 1)
        self.buttonSalirPause = Button(187, 279, self.imgSalir, 1)
        self.buttonReanudar = Button(190, 186, self.imgReanudar, 1)
        self.buttonSalirGameOver = Button(190, 360, self.imgSalir, 1)


    """ 
         este es el bucle principal del juego. Mientras la bandera "game_over"
          sea falsa, se llamarán los métodos eventsControl y "initComponents.
    """
    def mainLoop(self):
        #Dibujar Menu
        if self.menu_state == "main":
            self.drawMainMenu()
        #Juego
        elif self.menu_state == "game":
            if self.game_pause:
                self.drawMenuPause()
            elif self.game_win:
                self.drawWin()
            elif self.game_over:
                self.drawGameOver()
            else:
                self.drawGame()

        #if self.menu_state == "game":
        self.eventsControl()
        pygame.display.flip()
        self.clock.tick(30)

        #




    """
    controla los eventos que ocurren en el juego, como cerrar la ventana o presionar una tecla.
    """
    def eventsControl(self):
        if self.isResponse:
            self.checkChart()
        #Eventos Generales
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            #Eventos del juego
            if self.menu_state == "game":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.game_pause = True

                    if event.key == pygame.K_RETURN:
                        if self.game_win:
                            self.checUserName = True
                            self.game_win = False
                            self.resetWin = True
                            self.backToMenu()
                        else:
                            self.check_char = True

                    if event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                        self.userText = self.userText[:-1]
                    else:
                        if self.game_win:
                            self.userText += event.unicode
                        else:
                            if len(self.userText) < 1:
                                self.userText += event.unicode
            #Eventos en el ranking
            #if self.menu_state == "ranking":
            #    pass





    """
    dibuja la imagen de fondo y el jugador en la pantalla y actualiza el juego.
    """




    #Renderiza texto y lo dibuja
    def drawText(self, text, font, text_col,x,y):
        img = font.render(text, True, text_col)
        self.screen.blit(img, (x, y))



    def checkChart(self):
        if self.check_char:
            if self.isCorrect:
                self.soundCorrect.play()
            else:
                self.soundIncorrect.play()
                self.player.addArm()
            self.userText = ""
            self.check_char = False
            self.isResponse = False
        """change = 0
        for i in range(0, len(self.word)):
            if self.word[i].upper() == self.userText.upper():
                change += 1
                self.check[i] = 1
        if change != 0:
            return True
        else:
            self.lives -= 1
            return False
        """

    def backToMenu(self):
        self.userText = ""
        self.lives = 0
        self.check = {}
        self.word = ''
        self.menu_state = "main"
        self.resetWin = True

    #Dibuja el menu principal
    def drawMainMenu(self):
        if self.menu_state == "main":
            self.screen.blit(self.imgMainMenu, [0, 0])
            self.screen.blit(self.imgTitleMain, [250, 50])
            if self.buttonJugar.draw(self.screen):
                self.startTime = pygame.time.get_ticks()
                self.startGame()
                self.menu_state = "game"
            if self.buttonRanking.draw(self.screen):
                print("ranking")
            if self.buttonSalir.draw(self.screen):
                print(self.menu_state)
                print("Q pasa soy yo?")
                pygame.quit()
                sys.exit()


    #Dibuja la pantalla de game Over
    def drawGameOver(self):
        self.screen.blit(self.imgGameOver, [0, 0])
        if self.buttonSalirGameOver.draw(self.screen):
            self.resetWin = True
            self.game_over = False
            self.backToMenu()


    #Dibuja la pantalla de juego
    def drawGame(self):
        self.screen.blit(self.background, [0, 0])
        self.screen.blit(self.imgInputText, [350, 350])
        elapsedTime = pygame.time.get_ticks() - self.startTime
        self.timeRecord = self.font.render("Tiempo: {:.2f}".format(elapsedTime / 1000), True, RED)
        self.screen.blit(self.timeRecord, (20, 20))
        self.screen.blit(self.font.render("Vidas: " + str(self.lives), True, RED), (400, 20))
        self.text_screen = self.font.render(self.userText, True, BLACK)
        self.screen.blit(self.text_screen, [430, 340])
        self.drawBaseWord()
        self.drawWordOnBase()
        self.player.drawPlayer(self.screen)

    #Dibuja el menu de pausa
    def drawMenuPause(self):
        self.screen.blit(self.imgBackPause, [0, 0])
        if self.buttonReanudar.draw(self.screen):
            self.game_pause = False
        if self.buttonSalirPause.draw(self.screen):
            self.game_pause = False
            self.backToMenu()

    #Dibujar la pantalla de Win
    def drawWin(self):
        elapsedTime = pygame.time.get_ticks() - self.startTime
        self.totalTime = elapsedTime/1000
        self.screen.blit(self.imgWin,[0,0])
        self.user_name_screen = self.font.render(self.userText, True, BLACK)
        self.screen.blit(self.user_name_screen, [320, 310])
        self.screen.blit(self.font.render("Puntuación Total: " + str(self.totalScore), True, RED), (180, 420))




