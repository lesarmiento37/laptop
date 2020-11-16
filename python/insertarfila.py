import sqlite3

conexion = sqlite3.connect("leonardo.db")
cursor = conexion.cursor()
cursor.execute("INSERT INTO PERSONAS VALUES ('Leonardo', 'Sarmiento',30)")
conexion.commit()#para que guarde los datos que le hemos insertado
conexion.close()

