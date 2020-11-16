import pandas as pd
import numpy as np

lista_valores = np.random.randint(0,100,50)

lista_valores.resize(5,10)

dataframe = pd.DataFrame(lista_valores)

print(dataframe[dataframe > 50]) # vuelve nulos los valores que son menores de 50



