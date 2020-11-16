#Tenemos 3 clases 
#vamos a obtener un numero aleatorio de alumnos por clase
#np.random.randint(minimo,maximo,numero)

import pandas as pd
import numpy as np

minimo = 10
maximo = 40
numero = 3
alumnos = np.random.randint(minimo,maximo,numero)
clases = ['clase1', 'clase2', 'clase3']

serie = pd.Series(alumnos,index=clases)

