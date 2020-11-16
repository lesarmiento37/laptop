import sqlite3

conexion = sqlite3.connect("leonardo.db")
cursor = conexion.cursor()
cursor.execute("UPDATE PERSONAS SET edad = 27 WHERE nombre = 'Mabel'")

conexion.commit()
conexion.close()
