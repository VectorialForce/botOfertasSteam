import json
import random
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#Problema: Necesito tomar el titulo y link de 3 juegos e ir a steam argentina y
# obtener su precio regional


#importar lista de juegos e iterar para obtener 3 elementos aleatorios

with open('../juegos.json', 'r') as archivoJson:
    listaJuegos = json.load(archivoJson)

titulos = [(juego['title'], juego['link']) for juego in listaJuegos]
print(titulos[0])

link = "https://itad.link/018d9386-6bd3-714a-bcbf-26331e05748d/" #[juego['link'] for juego in listaJuegos]
print(link[0])

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
linkSteam = str(link)

driver.get(linkSteam)

precioUSD = driver.find_element(By.CSS_SELECTOR, ".discount_final_price")
resultado = precioUSD.text.strip("$ USD")
print(resultado)

time.sleep(100)