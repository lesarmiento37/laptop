
import sqlite3

conexion = sqlite3.connect("leonardo.db")
cursor = conexion.cursor()
cursor.execute("DELETE FROM PERSONAS WHERE nombre = 'Carolain'")
personas = cursor.fetchall()

for persona in personas:
        print(persona)
conexion.commit()
conexion.close()
