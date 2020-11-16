import moduloficheros

nombre_fichero = 'andrea.txt'
fichero = moduloficheros.Fichero(nombre_fichero)

texto = 'esta es la primera fila del fichero. \nEsta es la segunda fila.'
fichero.grabar_fichero(texto)

texto = '\nEste es el texto incluido en la tercera fila'
fichero.incluir_fichero(texto)

texto_leido = fichero.leer_fichero()
print(texto_leido)
