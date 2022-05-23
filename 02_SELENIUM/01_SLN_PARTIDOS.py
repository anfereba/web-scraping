import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

url_semilla = "https://www.adamchoi.co.uk/teamgoals/detailed"
path_driver = 'chromedriver.exe'

##Cargar driver
driver = webdriver.Chrome(path_driver)

##Inicializar Driver
driver.get(url_semilla)

all_matches_button = driver.find_element(By.XPATH, "//label[normalize-space()='All matches']")
all_matches_button.click()

## Capturar Lista desplegable de paises
dropwdown = Select(driver.find_element(By.XPATH, "//select[@id='country']"))

## Seleccionar valor de la lista desplegable
dropwdown.select_by_visible_text('Spain')

matches = driver.find_elements(By.XPATH, "//tr")

partidos = []
for match in matches:
    partidos.append(match.text)
    print(match.text)

driver.quit()
df = pd.DataFrame({'partidos':partidos})
print(df)
df.to_csv('partidos.csv', index=False)
