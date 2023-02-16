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
        ##intanciar clase bd

    def showView(self):
        self.view.sounBack.play(loops=-1)
        while not self.view.game_quit:
            self.view.mainLoop()
            self.eventsControl()

    def eventsControl(self):
        if self.view.resetWin:
            self.view.resetWin = False
            self.model.resetGame()
            self.view.resetView()

        if self.view.get_data_length:
            self.view.lenWord = len(self.model.getSecretWord()) #Longitud de la palabra
            self.view.lives = self.model.getLives() # Vidas iniciales
            self.view.get_data_length = False
        if self.view.check_char:
            #Cambiar condicional por verificacion de vidas
            if self.model.getLives() > 1:
                char = self.view.userText.lower()
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
                    #Se obtiene el nombre del usuario, las vidas y el tiempo
                    if self.view.checUserName:
                        userName = self.view.playerName
                        print(userName)
                        self.view.checUserName = False
                        self.view.game_win = False
                        self.view.resetWin = True
                    ## ESTEBAN --> guardar en base de datos self.bd_model.savePlayer(userName, self.model.score)

            else:
                self.view.game_over = True
        if self.view.menu_state == "ranking":
            ## ESTEBAN -->  Igualar self.view.players a 
            self.view.players = [(2, 'Manuel', 200), (3, 'Esteban', 150), (1, 'Tania', 100), (7, 'Santiago', 25), (8, 'Santiago', 25), (4, 'Malpik', 10)]




control = Controller()
control.showView()