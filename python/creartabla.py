import sqlite3

conexion2 = sqlite3.connect("leonardo.db")
cursor = conexion2.cursor()
cursor.execute("CREATE TABLE PERSONAS (nombre TEXT, apellido TEXT, edad INTEGER)")
conexion2.commit()
conexion2.close()