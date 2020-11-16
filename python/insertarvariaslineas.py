import sqlite3

conexion = sqlite3.connect("leonardo.db")
cursor = conexion.cursor()
lista_personas = [ ('Ruby' , 'Alvarez', 21),('Carolain', 'Jimenez', 25), ('Mabel','Sandoval',28)]
cursor.executemany("INSERT INTO PERSONAS VALUES (?,?,?)", lista_personas)
conexion.commit()
conexion.close()
