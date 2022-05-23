import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

## Inicializar clase options para ejecucion en 2do Plano

options = Options()
options.headless = False  ## Activa headless mode
## options.add_argument('window-size=1920x1080') ##Resolucion para pantalla

url_semilla = "https://www.audible.com/coming-soon?ref=a_search_t1_navTop_pl0cg1c0r1&pf_rd_p=9e018799-0a34-41a5-aa6e-54e9b77f2373&pf_rd_r=NMTHZG2Q4MFQSZDTE0Y1"
path_driver = 'chromedriver.exe'

##Cargar driver
driver = webdriver.Chrome(path_driver, options=options)

##Inicializar Driver
driver.get(url_semilla)

## Maximizar sitio web
driver.maximize_window()

## Paginacion

pagination = driver.find_element(By.XPATH, "//div[@class='linkListWrapper']//ul")
pages = pagination.find_elements(By.XPATH, "./li")
last_page = int(pages[-2].text)  ## Obtiene la Pag #60

current_page = 1
book_title = []
book_author = []
book_length = []

while current_page <= last_page:

    print(current_page, 'de', last_page)
    ## Contenedor de todos los li (UL)

    container = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//div[@data-widget='productList']"))
    )

    ## Container = driver.find_element(By.XPATH, "//div[@data-widget='productList']")

    products = WebDriverWait(container, 5).until(
        EC.presence_of_all_elements_located((By.XPATH, "./li"))
    )

    ## products = container.find_elements(By.XPATH, "./li")

    for product in products:
        print("===========================================================================")
        book_title.append(product.find_element(By.XPATH, ".//h3").text)
        print("Titulo:", product.find_element(By.XPATH, ".//h3").text)
        book_author.append(product.find_element(By.XPATH, ".//li[contains(@class,'author')]//a").text)
        print("Autor:", product.find_element(By.XPATH, ".//li[contains(@class,'author')]//a").text)
        book_length.append(product.find_element(By.XPATH, ".//li[contains(@class,'runtime')]/span").text)
        print("Duracion:", product.find_element(By.XPATH, ".//li[contains(@class,'runtime')]/span").text)

    current_page += 1

    try:
        next_page = driver.find_element(By.XPATH, "//span[contains(@class,'next')]/a")
        next_page.click()
    except:
        pass

driver.quit()

dict_books = {'Titulo': book_title, 'Autor': book_author, 'Duracion': book_length}
df_books = pd.DataFrame.from_dict(dict_books)
df_books.to_csv('libros_pagina.csv', index=False)
