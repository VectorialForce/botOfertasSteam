import json

from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def ingresarEnITAD():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    link = "https://isthereanydeal.com/deals/#filter:N4IgzgFg9gDmIC4DaA2AjAXQDQgMYFcAXRUAWwEsA7RATgAYdSBDAD0TTroF8ug="

    try:
        driver.get(link)
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.title")))
    except WebDriverException as e:
        if "net::ERR_INTERNET_DISCONNECTED" in str(e):
            print("No hay conexión a internet.")
        else:
            print("Error WebDriver:", e)

    return driver

def guardarJuegos(driver):
    juegos = driver.find_elements(By.CSS_SELECTOR, "div.js-gid")
    data = []
    indice = 0
    for juego in juegos:
        try:
            titulo = juego.find_element(By.CSS_SELECTOR, "a.title").text.strip()
            precio = juego.find_element(By.CSS_SELECTOR, "span.deal__new").text.strip("$")
            link = juego.find_element(By.CSS_SELECTOR, "a.deal__main").get_attribute("href")
            indice += 1

            data.append({"indice": indice, "titulo": titulo, "precio": precio, "link": link})

            print(f"{indice}: {titulo} -> {precio} -> {link}")
        except Exception as e:
            print("Error leyendo un juego:", e)

    with open("data/juegos.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def scrapearITAD():
    driver = ingresarEnITAD()
    guardarJuegos(driver)
    driver.quit()
    print("Valores actualizados")

scrapearITAD()