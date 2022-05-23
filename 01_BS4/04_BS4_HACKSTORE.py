from bs4 import BeautifulSoup
import requests, re
import pandas as pd



def extraer_genero(cadena):
    try:
        return ' '.join(re.findall('(?<=Genero: ).*.', cadena))
    except AttributeError:
        pass

def extraer_pais(cadena):
    try:
        return ' '.join(re.findall('(?<=País: ).*.', cadena))
    except AttributeError:
        pass

def extraer_duracion(cadena):
    try:
        return ' '.join(re.findall('(?<=Duración: ).*.', cadena))
    except AttributeError:
        pass

def extraer_anio(cadena):
    try:
        return ' '.join(re.findall('(?<=Año: ).*.', cadena))
    except AttributeError:
        pass

def extraer_director(cadena):
    try:
        return ' '.join(re.findall('(?<=Director: ).*.', cadena))
    except AttributeError:
        pass

##Declaracion de variables

titulos = []
generos = []
paises = []
duraciones = []
anios = []
directores = []

urL_semilla = 'https://hackstore.st/peliculas/'
result = requests.get(urL_semilla)
content = result.text
soup = BeautifulSoup(content, 'lxml')

## Paginacion

pagination = soup.find('a', class_='numbered page-number-last')
ultima_pagina = int(pagination['href'].split('/')[-2])

## Por cada pagina
for page in range(1,ultima_pagina+1):
    result = requests.get(f'{urL_semilla}page/{page}/')
    content = result.text
    soup = BeautifulSoup(content, 'lxml')

    peliculas_pag_actual = soup.findAll('div', class_='movie-back')

    ## Extrae los links de las peliculas de la pagina actual

    links_peliculas_pag_actual = []

    for pelicula in peliculas_pag_actual:
        link_pelicula = pelicula.find('a', href=True)
        links_peliculas_pag_actual.append(link_pelicula['href'])

    ## Web Scraping para cada link de la pelicula

    for link in links_peliculas_pag_actual:
        try:
            link_pelicula = link
            result = requests.get(link_pelicula)
            content = result.text
            soup = BeautifulSoup(content, 'lxml')

            box = soup.find('div', class_='watch-text')
            texto_pelicula = box.get_text()

            titulo_pelicula = soup.find('h1').get_text()
            pais_pelicula = extraer_pais(texto_pelicula)
            duracion_pelicula = extraer_duracion(texto_pelicula)
            anio_pelicula = extraer_anio(texto_pelicula)
            director_pelicula = extraer_director(texto_pelicula)

            titulos.append(titulo_pelicula)
            anios.append(anio_pelicula)
            paises.append(pais_pelicula)
            duraciones.append(duracion_pelicula)
            directores.append(director_pelicula)

            print("----------------------------------------------------------------------------")
            print(f'Titulo pelicula: {titulo_pelicula}')
            print(f'Pais: {pais_pelicula}')
            print(f'Duracion: {duracion_pelicula}')
            print(f'Anio: {anio_pelicula}')
            print(f'Director: {director_pelicula}')
        except:
            pass


dict_peliculas = {'Titulo':titulos,'Pais':paises,'Duracion':duraciones,'Año':anios,'Director':directores}
df_peliculas = pd.DataFrame.from_dict(dict_peliculas)
df_peliculas.to_csv('peliculitas.csv', index=False)

