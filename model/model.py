import random
from urllib import request
import requests
import asyncio


# Lista de palabras posibles


async def requestWord():
    url = "https://clientes.api.greenborn.com.ar/public-random-word?c=1&l=13"

    # Realizar una solicitud GET a la API
    response = requests.get(url)
    # Verificar si la solicitud tuvo éxito
    if response.status_code == 200:
        # Procesar los datos de la respuesta
        data = response.json()
        print(data)
        init_game(data[0])
    else:
        # Mostrar un mensaje de error
        print("Error al consumir la API. Codigo de estado:", response.status_code)



def init_game(palabra_secreta):
    # Seleccionar una palabra al azar

    # Inicializar variables
    fallos = 0
    adivinadas = []
    # Bucle principal del juego
    while fallos < 5:
        exito = False
        for letra in palabra_secreta:
            if letra in adivinadas:
                print(letra, end=" ")
            else:
                print("_", end=" ")
        print("")
        print("Letras adivinadas:", adivinadas)

        # Obtener una letra del usuario
        letra = input("Adivina una letra: ")
        if len(letra) > 1 and len(letra) == len(palabra_secreta):
            if letra == palabra_secreta:
                ganado = True
                print("Felicidades! Has adivinado la palabra secreta!")
                break
            else:
                exito = False
                fallos += 1
                print(f"Lo siento, esa no es la palabra secreta. Vidas: {6-fallos}")

        elif len(letra) >1 and len(letra) != len(palabra_secreta):
            print(f"Porfavor digita una letra o la cantidad exacta de letras que tiene la palabra secreta ({len(palabra_secreta)})...")
        else:

            # Verificar si la letra está en la palabra secreta
            if letra in palabra_secreta:
                exito = True
                adivinadas.append(letra)
                print(f"Buen trabajo! La letra esta en la palabra. Vidas: {6-fallos}")
            else:
                exito = False
                fallos += 1
                print(f"Lo siento, la letra no esta en la palabra. Vidas: {6-fallos}")

            # Verificar si el usuario ha adivinado todas las letras
            ganado = True
            for letra in palabra_secreta:
                if letra not in adivinadas:
                    ganado = False
                    break

            # Mostrar un mensaje si el usuario gana
            if ganado:
                print("Felicidades! Has adivinado todas las letras de la palabra secreta!")
                break

    # Mostrar un mensaje si el usuario pierde
    if not ganado:
        print("Lo siento, has agotado todas tus oportunidades. La palabra secreta era '{}'.".format(palabra_secreta))

asyncio.run(requestWord())
