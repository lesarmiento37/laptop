import sqlite3

conexion = sqlite3.connect("leonardo.db")
cursor = conexion.cursor()
cursor.execute("SELECT * FROM PERSONAS")
personas = cursor.fetchall()

for persona in personas:
	print(persona)
#conexion.commit()-> esto es solo cuando se actualiza
conexion.close()
