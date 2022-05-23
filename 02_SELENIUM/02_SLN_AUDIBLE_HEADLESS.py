import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

## Inicializar clase options para ejecucion en 2do Plano

options = Options()
options.headless = True ## Activa headless mode
options.add_argument('window-size=1920x1080') ##Resolucion para pantalla

url_semilla = "https://www.audible.com/search"
path_driver = 'chromedriver.exe'

##Cargar driver
driver = webdriver.Chrome(path_driver, options=options)

##Inicializar Driver
driver.get(url_semilla)

## Maximizar sitio web
## driver.maximize_window()

## Contenedor de todos los li (UL)

container = driver.find_element(By.XPATH, "//div[@class='adbl-impression-container ']")

## Seleccion de cada li
products = container.find_elements(By.XPATH, "./li")

book_title = []
book_author = []
book_length = []

for product in products:
    print("===========================================================================")
    book_title.append(product.find_element(By.XPATH, ".//h3").text)
    print("Titulo:",product.find_element(By.XPATH, ".//h3").text)
    book_author.append(product.find_element(By.XPATH, ".//li[contains(@class,'author')]//a").text)
    print("Autor:", product.find_element(By.XPATH, ".//li[contains(@class,'author')]//a").text)
    book_length.append(product.find_element(By.XPATH, ".//li[contains(@class,'runtime')]/span").text)
    print("Duracion:",product.find_element(By.XPATH, ".//li[contains(@class,'runtime')]/span").text)

driver.quit()

dict_books = {'Titulo':book_title,'Autor':book_author,'Duracion':book_length}
df_books = pd.DataFrame.from_dict(dict_books)
df_books.to_csv('libros.csv', index=False)