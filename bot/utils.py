import json
import random

def getJuego(indice):

    with open('../data/juegos.json', 'r') as archivoJson:
        listaDeOfertas = json.load(archivoJson)

    juego = listaDeOfertas[indice - 1]

    titulo = juego['titulo']
    precio = juego['precio']
    link = juego['link']

    tweet = (
    f"🚨 Hoy tenes en oferta {titulo} por ${precio} USD\n"
    f"(Precio estimado, puede variar según región)\n"
    f"{link}\n"
    )

    return tweet

def getJuegoAleatorio():

    numeroAleatorio = random.randint(1,15)

    return getJuego(numeroAleatorio)