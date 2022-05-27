import time

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

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)


## Retorna el usuario y su tweet
def get_tweet(element):
    try:
        user = element.find_element_by_xpath(".//span[contains(text(), '@')]").text
        text = element.find_element_by_xpath(".//div[@lang]").text
        tweets_data = [user, text]
    except:
        tweets_data = ['user', 'text']
    return tweets_data


## Click en Boton Login

login = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//a[@href='/login']"))
)

login.click()

## Escribe Username

login_input = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//input[@autocomplete='username']"))
)

login_input.send_keys('@AndresP57928891')

## Click en siguiente

next_button = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Siguiente')]"))
)

next_button.click()

## Escribir contraseña

password_input = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//input[@name='password']"))
)

password_input.send_keys('culosclan')

## Click en Login

login_button = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Iniciar sesión')]"))
)

login_button.click()

## Hacer una busqueda

search_box = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search Twitter' or @placeholder = 'Buscar en "
                                              "Twitter']"))
)

search_box.send_keys('Colombia')
search_box.send_keys(Keys.ENTER)

user_data = []
text_data = []
tweet_ids = set()

scrolling = True

## Scrolling

while scrolling:

    ## Extrae los tweets de la pagina actual

    tweets = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.XPATH, '//article[@role="article"]'))
    )

    print(len(tweets))
    ## Selecciona n tweets por cada scrolling de pagina
    for tweet in tweets:
        tweet_list = get_tweet(tweet)
        tweet_id = ''.join(tweet_list)
        if tweet_id not in tweet_ids:
            tweet_ids.add(tweet_id)
            user_data.append(tweet_list[0])
            text = " ".join(tweet_list[1].split())
            text_data.append(text)

    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            scrolling = False
            break
        else:
            last_height = new_height
            break

driver.quit()

df_tweets = pd.DataFrame({'user': user_data, 'text': text_data})
df_tweets.to_csv('tweets_infinite_scrolling.csv', index=False)
print(df_tweets)
