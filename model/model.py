from urllib import request
import requests
import asyncio


# Lista de palabras posibles

class Model:

    puntuacion = 0
    isGameOver = False
    fallos = 0
    adivinadas = [] ##Las letras que ha adivinado
    palabra_secreta = "" ##Palabra a adivinar
    diccionario = {} ##{posicion de letra adivinada: letra adivinada} 
    """
    Ej: palabra_secreta = "carrusel"
        adivinadas = ["c","r"]
        diccionario = {0:"c",
                       2:"r",
                       3:"r"}
    """
    
    
    
    
    def __init__(self):
        while(not self.isGameOver):
            asyncio.run(self.requestWord())
            self.fallos = 0
            self.adivinadas = []
            self.diccionario = {}
        self.puntuacion = 0
        
    async def requestWord(self):
        url = "https://clientes.api.greenborn.com.ar/public-random-word?c=1&l=8"

        # Realizar una solicitud GET a la API
        response = requests.get(url)
        # Verificar si la solicitud tuvo éxito
        if response.status_code == 200:
            # Procesar los datos de la respuesta
            data = response.json()
            print(data)
            self.palabra_secreta = data[0]
            self.init_game()
        else:
            # Mostrar un mensaje de error
            print("Error al consumir la API. Codigo de estado:", response.status_code)



    def init_game(self):
        # Bucle principal del juego
        while self.fallos < 5:
            exito = False
            for letra in self.palabra_secreta:
                if letra in self.adivinadas:
                    print(letra, end=" ")
                else:
                    print("_", end=" ")
            print("")
            print("Letras adivinadas:", self.adivinadas)
            print(self.diccionario)

            # Obtener una letra del usuario
            letra = input("Adivina una letra: ")
            if len(letra) > 1 and len(letra) == len(self.palabra_secreta):
                if letra == self.palabra_secreta:
                    ganado = True
                    print("Felicidades! Has adivinado la palabra secreta!")
                    self.puntuacion += (10*(len(self.palabra_secreta)-len(self.adivinadas)))
                    print(f"Puntuación: {self.puntuacion}")
                    break
                else:
                    exito = False
                    self.fallos += 1
                    print(f"Lo siento, esa no es la palabra secreta. Vidas: {5-self.fallos}")
                    print(f"Puntuación: {self.puntuacion}")


            elif len(letra) >1 and len(letra) != len(self.palabra_secreta):
                print(f"Porfavor digita una letra o la cantidad exacta de letras que tiene la palabra secreta ({len(self.palabra_secreta)})...")
            else:

                # Verificar si la letra está en la palabra secreta
                if letra in self.palabra_secreta:
                    exito = True
                    self.adivinadas.append(letra)
                    indexes = [i for i, c in enumerate(self.palabra_secreta) if c == letra]
                    for i in indexes:
                        self.diccionario[i] = letra
                    print(f"Buen trabajo! La letra esta en la palabra. Vidas: {5-self.fallos}")
                    self.puntuacion += 10
                    print(f"Puntuación: {self.puntuacion}")

                else:
                    exito = False
                    self.fallos += 1
                    print(f"Lo siento, la letra no esta en la palabra. Vidas: {5-self.fallos}")
                    print(f"Puntuación: {self.puntuacion}")

                # Verificar si el usuario ha adivinado todas las letras
                ganado = True
                for letra in self.palabra_secreta:
                    if letra not in self.adivinadas:
                        ganado = False
                        break

                # Mostrar un mensaje si el usuario gana
                if ganado:
                    print("Felicidades! Has adivinado todas las letras de la palabra secreta!")
                    print(f"Puntuación: {self.puntuacion}")
                    break

        # Mostrar un mensaje si el usuario pierde
        if not ganado:
            print("Lo siento, has agotado todas tus oportunidades. La palabra secreta era '{}'.".format(self.palabra_secreta))
            self.isGameOver = True

##Model()
