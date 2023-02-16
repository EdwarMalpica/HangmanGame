from urllib import request
import requests ## pip install requests
import asyncio
import random


# Lista de palabras posibles

class Model:

    """
    Ej: palabra_secreta = "carrusel"
        adivinadas = ["c","r"]
        diccionario = {0:"c",
                       2:"r",
                       3:"r"}
    """
    
    def __init__(self): 
        self.palabra_secreta = "" ##Palabra a adivinar
        asyncio.run(self.requestWord())      
        self.adivinadas = [] ##Las letras que ha adivinado
        self.diccionario = {} ##{posicion de letra adivinada: letra adivinada} 
        self.ganado = False
        self.exito = False
        self.fallos = 0
        self.score = 0
        
    async def requestWord(self):
        leng = random.randint(4,8)
        url = f"https://clientes.api.greenborn.com.ar/public-random-word?c=1&l={leng}"
        # Realizar una solicitud GET a la API
        response = requests.get(url)
        # Verificar si la solicitud tuvo éxito
        if response.status_code == 200:
            # Procesar los datos de la respuesta
            data = response.json()
            self.palabra_secreta = data[0]
            print(self.palabra_secreta)
        else:
            # Mostrar un mensaje de error
            print("Error al consumir la API. Codigo de estado:", response.status_code)


    def checkSuccess(self, letra):
        # Verificar si la letra está en la palabra secreta
        if letra in self.palabra_secreta:
            self.exito = True
            self.adivinadas.append(letra)
            indexes = [i for i, c in enumerate(self.palabra_secreta) if c == letra]
            for i in indexes:
                self.diccionario[i] = letra
        else:
            self.exito = False
            self.fallos += 1
        # Verificar si el usuario ha adivinado todas las letras
        self.ganado = True
        for letra in self.palabra_secreta:
            if letra not in self.adivinadas:
                self.ganado = False
                break
    
    def getLetter(self, letra):
        if self.fallos < 5:
            self.exito = False
            if len(letra) > 1 and len(letra) == len(self.palabra_secreta):
                if letra == self.palabra_secreta:
                    self.ganado = True
                else:
                    self.exito = False
                    self.fallos += 1
            elif len(letra) >1 and len(letra) != len(self.palabra_secreta):
                self.fallos += 1
            else:
                self.checkSuccess(letra)
    
    def getDiccionario(self):
        return self.diccionario

    def getSecretWord(self):
        return self.palabra_secreta

    def getLives(self):
        return 5 - self.fallos
    def isSuccess(self):
        return self.exito
    
    def resetGame(self):
        asyncio.run(self.requestWord())      
        self.adivinadas = [] ##Las letras que ha adivinado
        self.diccionario = {} ##{posicion de letra adivinada: letra adivinada} 
        self.ganado = False
        self.exito = False
        self.fallos = 0
        self.score = 0

    def calculateScore(self, lives, time):
        total = 0
        total += lives*50
        total += len(self.palabra_secreta)*20
        ##puntuacion en funcion del tiempo
        total += self.calculateScoreByTime(time)
        self.score = total
        print(self.score)

    def calculateScoreByTime(self, time):
        if time < 0:
            return 0  # Si el tiempo es negativo, la puntuación es cero
        elif time <= 10:
            return 300  # Si el tiempo es de 10 segundos o menos, la puntuación es de 100 puntos
        else:
            return max(0, 100 - (time - 10))  
        