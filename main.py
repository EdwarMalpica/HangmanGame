import threading
import time
from model.model import Model

from view.MainView import MainView

class Controller:

    def __init__(self):
        #Variable Modelo
        self.model = Model()
        print(self.model.getSecretWord())
        print(len(self.model.getSecretWord()))
        self.view = MainView()

    def showView(self):
        self.view.sounBack.play(loops=-1)
        while not self.view.game_quit:
            self.view.mainLoop()
            self.eventsControl()

    def eventsControl(self):
        if self.view.buttonSalirGameOver.draw(self.view.screen) or self.view.buttonSalirPause.draw(self.view.screen):
            self.model.resetGame()
            self.view.resetView()

        if self.view.get_data_length:
            self.view.lenWord = len(self.model.getSecretWord()) #Longitud de la palabra
            self.view.lives = self.model.getLives() # Vidas iniciales
            self.view.get_data_length = False
        if self.view.check_char:
            #Cambiar condicional por verificacion de vidas
            if self.model.getLives() > 1:
                char = self.view.userText
                #Se necesita si la palabra esta o no
                self.model.getLetter(char)
                self.view.isCorrect = self.model.isSuccess()
                #Se necesita el diccionario
                self.view.check = self.model.getDiccionario()
                #Vidas Actuales
                self.view.lives = self.model.getLives()
                #Al finalizar se debe actualizar la variable response
                self.view.isResponse = True

                ##Establecer condicion de victoria
                print(self.model.ganado)
                if self.model.ganado:
                    lives = self.view.lives
                    timeUser = self.view.totalTime
                    self.model.calculateScore(lives, timeUser)
                    self.view.totalScore = self.model.score
                    self.view.game_win = True
                    self.view.checUserName = True
                    #Se obtiene el nombre del usuario, las vidas y el tiempo
                    userName = self.view.userText
                    ##guardar en base de datos self.bd_model.savePlayer(userName,score)

            else:
                self.view.game_over = True
        if self.view.game_over:
            #Obtener Puntuacion
            pass




control = Controller()
control.showView()