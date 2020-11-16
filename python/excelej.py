#leer ficheros excel


import pandas as pd
excel = pd.ExcelFile('/home/leonardo/poblacion.xlsx')
dataframe = excel.parse('Hoja 1')
ciudad = dataframe['Ciudad más poblada'][3] #ciudad mas poblada de la tabla
print(dataframe)	
print(ciudad)
