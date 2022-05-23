import pandas as pd

paises = ["Mexico","Colombia","Peru","Argentina"]
poblacion = [13123,24213,5435354,1312333]

dict_poblacion = {'Paises':paises,'Poblacion':poblacion}
df_poblacion = pd.DataFrame.from_dict(dict_poblacion)
df_poblacion.to_csv('poblacion.csv', index=False)
