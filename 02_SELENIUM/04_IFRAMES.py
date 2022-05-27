import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

## Inicializar clase options para ejecucion en 2do Plano

opts = Options()

opts.add_argument(
    "user_agent=Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 "
    "Safari/537.1 "
)


url_selector = "file:///C:/Users/anfer/OneDrive/Escritorio/index.html"
path_driver = "chromedriver.exe"
driver = webdriver.Chrome(path_driver, chrome_options=opts)
driver.get(url_selector)
driver.switch_to.frame(driver.find_element(By.XPATH, "/html/body/iframe"))

boton = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='gsc-i-id2']"))
)
boton.send_keys("Molly xd")