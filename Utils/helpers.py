import json

def obtenerTresJuegos(contador):

    fin = contador * 3
    inicio = fin - 3

    with open('juegos.json', 'r') as archivoJson:
        listaJuegos = json.load(archivoJson)

    seleccionar = listaJuegos[0]

    lista = f"{seleccionar['titulo']} - ${seleccionar['precio']} - {seleccionar['link']}"

    return lista