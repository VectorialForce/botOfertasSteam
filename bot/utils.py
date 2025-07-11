import json

def getJuego(indice):

    with open('juegos.json', 'r') as archivoJson:
        listaDeOfertas = json.load(archivoJson)

    juego = listaDeOfertas[indice - 1]

    return f"{juego['titulo']} - ${juego['precio']} - {juego['link']}"