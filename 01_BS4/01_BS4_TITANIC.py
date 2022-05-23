from bs4 import BeautifulSoup
import requests

url_webstite = 'https://subslikescript.com/movie/Titanic-120338'
result = requests.get(url_webstite) ## Obtiene la pagina

content = result.text ## Obtener texto de el resultado
soup = BeautifulSoup(content,'lxml') ## Contenido + Parser

box = soup.find('article',class_='main-article') ## Obtiene todo el html dentro de article

title = box.find('h1').get_text() ##Obtiene H1
texto = box.find('p').get_text(strip=True, separator=' ') ##Obtiene texto

## Guardar texto

with open(f'{title}.txt','w') as file:
    file.write(texto)


