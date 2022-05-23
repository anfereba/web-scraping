import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

## Inicializar clase options para ejecucion en 2do Plano


url_twitter = "https://twitter.com/"
path_driver = "chromedriver.exe"
driver = webdriver.Chrome(path_driver)
driver.get(url_twitter)
driver.maximize_window()

## Click en Login

login = WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.XPATH, "//a[@href='/login']"))
)

login.click()


login_input = WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.XPATH, "//input[@autocomplete='username']"))
)

login_input.send_keys('@AndresP57928891')

next_button = WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Siguiente')]"))
)

next_button.click()

## Contraseña

password_input = WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.XPATH, "//input[@name='password']"))
)

password_input.send_keys('culosclan')

## Click en Login

login_button = WebDriverWait(driver,20).until(
    EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Iniciar sesión')]"))
)

login_button.click()

## Hacer una busqueda

search_box = WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search Twitter' or @placeholder = 'Buscar en "
                                              "Twitter']"))
)

search_box.send_keys('Bogota')
search_box.send_keys(Keys.ENTER)

tweets = WebDriverWait(driver,5).until(
    EC.presence_of_all_elements_located((By.XPATH, '//article[@role="article"]'))
)

for tweet in tweets:
