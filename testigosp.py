import moduloficheros
from os import *
var = []
ruta = ["/home/dionis/192.168.19.60.txt","/home/dionis/192.168.19.52.txt","/home/dionis/192.168.19.244.txt","/home/dionis/192.168.19.197.txt","/home/dionis/192.168.19.181.txt","/home/dionis/192.168.19.152.txt","/home/dionis/192.168.19.87.txt","/home/dionis/192.168.19.153.txt","/home/dionis/192.168.21.103.txt","/home/dionis/192.168.35.212.txt","/home/dionis/192.168.4.30.txt","/home/dionis/192.168.4.130.txt","/home/dionis/192.168.4.163.txt","/home/dionis/192.168.4.26.txt","/home/dionis/192.168.4.100.txt","/home/dionis/192.168.9.81.txt","/home/dionis/192.168.9.199.txt","/home/dionis/192.168.9.140.txt","/home/dionis/192.168.9.79.txt","/home/dionis/192.168.16.170.txt","/home/dionis/192.168.16.56.txt","/home/dionis/192.168.1.54.txt","/home/dionis/192.168.1.46.txt","/home/dionis/192.168.1.32.txt","/home/dionis/192.168.1.78.txt","/home/dionis/192.168.5.193.txt","/home/dionis/192.168.5.140.txt","/home/dionis/192.168.5.89.txt","/home/dionis/192.168.30.33.txt"]
nombres = ["manjui","quinini","cerro negro","guaduas","flores","sarzo","granada","flandes","tierra morada","bethesda","guadalupe","santo domingo","alpes","boqueron","av 19","suba 2","tibitoc","horgano","junin","cazadores","margarita","picacho","soldapedro","petalos","tablazo","soda","suba1","cucunuba","tres cruces"]

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
			#print(nombres[i] + "    |    " + nombre4 +"   "+ruta[i])
			print(nombre4)
			var.append(nombre3)
print("\n")
print(*var,sep=";")

