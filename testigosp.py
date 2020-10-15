import moduloficheros
from os import *
import pandas as pd
import xlsxwriter
var = []
ruta = ["/home/dionis/192.168.19.60.txt","/home/dionis/192.168.19.52.txt","/home/dionis/cerro2.txt","/home/dionis/192.168.19.65.txt","/home/dionis/192.168.19.181.txt","/home/dionis/sarzo.txt","/home/dionis/192.168.19.87.txt","/home/dionis/192.168.19.153.txt","/home/dionis/192.168.21.103.txt","/home/dionis/192.168.35.212.txt","/home/dionis/192.168.4.30.txt","/home/dionis/192.168.4.130.txt","/home/dionis/192.168.4.163.txt","/home/dionis/192.168.4.26.txt","/home/dionis/192.168.4.100.txt","/home/dionis/192.168.9.81.txt","/home/dionis/192.168.9.199.txt","/home/dionis/192.168.9.140.txt","/home/dionis/192.168.9.79.txt","/home/dionis/192.168.16.170.txt","/home/dionis/192.168.16.117.txt","/home/dionis/192.168.1.54.txt","/home/dionis/192.168.1.43.txt","/home/dionis/192.168.1.32.txt","/home/dionis/192.168.1.78.txt","/home/dionis/192.168.5.193.txt","/home/dionis/192.168.5.140.txt","/home/dionis/192.168.5.89.txt","/home/dionis/192.168.30.33.txt","/home/dionis/192.168.35.63.txt"]
nombres = ["Manjui","Quinini","Cerro Negro","Guaduas","Flores","Sarzo","Granada","Flandes","Tierra Morada","Bethesda","Guadalupe","Santo domingo","Alpes","Boqueron","Av 19","Suba 2","Tibitoc","Horgano","Junin","Cazadores","Margarita","Picacho","Soldapedro","Petalos","Tablazo","Soda","Suba1","Cucunuba","Tres Cruces","Eduardo Porras"]
lista_nombres = ['Testigos']

system('rm testigos.xlsx')
for i in range (0, len(ruta)):
	fichero = moduloficheros.Fichero(ruta[i])
	texto = fichero.leer_fichero()
	linea = texto.split("\n")
	for n in range(0,len(linea)):
		if("voltage:" in linea[n]):
			nombre = linea[n].replace(" ","")
			nombre2 = nombre.replace("voltage:","") 		
			nombre3 = nombre2.replace("V","")
			nombre4 = nombre3.replace(".",",")
			print(nombres[i] + "    |    " + nombre4 +"   "+ruta[i])
			#print(nombre4)
			var.append(nombre3)
# Create a Pandas dataframe from some data.
testigo =  pd.DataFrame(var,nombres, columns=lista_nombres)

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('testigos.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
testigo.to_excel(writer, sheet_name='Hoja1')

# Get the xlsxwriter workbook and worksheet objects.
workbook  = writer.book
worksheet = writer.sheets['Hoja1']
format1 = workbook.add_format({'align' : 'center'})


# Set the column width and format.
worksheet.set_column('A:A', 15, format1)
worksheet.set_column('B:B', 10, format1)
#worksheet.set_column('C:C', 30, format1)
worksheet2 = workbook.add_worksheet('Hoja2')
row = 0
for n in (var):
	worksheet2.write(0,row,n)
	row +=1

writer.save()

print(testigo)
system('expect ftp.sh')


