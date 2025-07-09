import json

def obtenerTresJuegos(contador):

    fin = contador * 3
    inicio = fin - 3

    with open('juegos.json', 'r') as archivoJson:
        listaJuegos = json.load(archivoJson)

    seleccionar = listaJuegos[inicio:fin]

    for juego in seleccionar:
        print(f"{juego['indice']}: {juego['titulo']} - {juego['precio']}")

