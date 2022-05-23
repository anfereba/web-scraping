from bs4 import BeautifulSoup
import requests

root = 'https://subslikescript.com/'  ## Raiz del WebSite
url_webstite = f'{root}/movies'
result = requests.get(url_webstite)  ## Obtiene la pagina

content = result.text  ## Obtener texto de el resultado
soup = BeautifulSoup(content, 'lxml')  ## Contenido + Parser

box = soup.find('article', class_='main-article')  ## Obtiene todo el html dentro de article

## Obtiene todas las etiquetas 'a' dentro de la caja en una lista
link_titles = box.findAll('a', href=True)  ## (etiqueta, atributo a obtener)

links = []

## Agrega los valores del atributo href a una lista

for link_title in link_titles:
    links.append(link_title['href'])
    ## print(link_title['href']) ## Obtenemos el HREF de cada link

## Web Scraping para cada link

for link in links:
    website = f'{root}/{link}'
    result = requests.get(website)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')

    box = soup.find('article', class_='main-article')

    title = box.find('h1').get_text()
    texto = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

    ## Guardar texto

    with open(f'{title}.txt', 'w', encoding='utf-8') as file:
        file.write(texto)



