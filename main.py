import threading
import time

from view.MainView import MainView

class Controller:

    def __init__(self):
        #Variable Modelo
        self.view = MainView()


    def showView(self):
        self.view.sounBack.play(loops=-1)
        while not self.view.game_quit:
            self.view.mainLoop()
            self.eventsControl()



    def eventsControl(self):
        if self.view.get_data_length:
            self.view.lenWord = 6 #Longitud de la palabra
            self.view.lives = 5 # Vidas iniciales
            self.view.get_data_length = False
        if self.view.check_char:
            #Cambiar condicional por verificacion de vidas
            if not self.view.game_over:
                char = self.view.userText
                #Se necesita si la palabra esta o no
                self.view.isCorrect = False
                #Se necesita el diccionario
                self.view.check = {}
                #Vidas Actuales
                self.view.lives = 4
                #Al finalizar se debe actualizar la variable response
                self.view.isResponse = True

                ##Establecer condicion de victoria

                if self.view.game_win:
                    if self.view.checUserName:
                        #Se obtiene el nombre del usuario, las vidas y el tiempo
                        userName = self.view.userText
                        lives = self.view.lives
                        timeUser = self.view.totalTime

            else:
                pass
                #self.view.game_over = True
        if self.view.game_over:
            #Obtener Puntuacion
            pass




control = Controller()
control.showView()