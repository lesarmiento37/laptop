import ficheros
rutas = ["/home/dionis/mo192.168.16.111.txt","/home/dionis/mo192.168.16.93.txt","/home/dionis/mo192.168.16.183.txt","/home/dionis/mo192.168.16.77.txt","/home/dionis/mo192.168.16.113.txt","/home/dionis/mo192.168.16.12.txt","/home/dionis/mo192.168.16.145.txt","/home/dionis/mo192.168.16.30.txt","/home/dionis/mo192.168.16.124.txt","/home/dionis/mo192.168.16.151.txt","/home/dionis/mo192.168.16.53.txt","/home/dionis/mo192.168.16.98.txt","/home/dionis/mo192.168.16.160.txt","/home/dionis/mo192.168.16.45.txt","/home/dionis/mo192.168.16.14.txt","/home/dionis/mo192.168.16.188.txt","/home/dionis/mo192.168.16.38.txt","/home/dionis/mo192.168.16.39.txt","/home/dionis/mo192.168.16.17.txt","/home/dionis/mo192.168.16.176.txt","/home/dionis/mo192.168.16.216.txt","/home/dionis/mo192.168.16.23.txt","/home/dionis/mo192.168.16.160.txt","/home/dionis/mo192.168.16.74.txt","/home/dionis/mo192.168.16.195.txt","/home/dionis/mo192.168.16.27.txt","/home/dionis/mo192.168.16.240.txt","/home/dionis/mo192.168.16.218.txt","/home/dionis/mo192.168.16.57.txt","/home/dionis/mo192.168.16.116.txt","/home/dionis/mo192.168.16.233.txt","/home/dionis/mo192.168.16.22.txt"]
rutas2 = ["/home/dionis/mo192.168.21.84.txt","/home/dionis/mo192.168.21.153.txt","/home/dionis/mo192.168.21.102.txt","/home/dionis/mo192.168.21.158.txt","/home/dionis/mo192.168.21.32.txt","/home/dionis/mo192.168.21.13.txt","/home/dionis/mo192.168.21.141.txt","/home/dionis/mo192.168.21.200.txt","/home/dionis/mo192.168.21.63.txt","/home/dionis/mo192.168.21.169.txt","/home/dionis/mo192.168.21.59.txt","/home/dionis/mo192.168.21.131.txt","/home/dionis/mo192.168.21.91.txt","/home/dionis/mo192.168.21.52.txt","/home/dionis/mo192.168.21.198.txt","/home/dionis/mo192.168.21.115.txt","/home/dionis/mo192.168.21.81.txt","/home/dionis/mo192.168.21.82.txt"] 
rutas3 = ["/home/dionis/mo192.168.19.141.txt","/home/dionis/mo192.168.19.85.txt","/home/dionis/mo192.168.19.131.txt","/home/dionis/mo192.168.19.124.txt","/home/dionis/mo192.168.19.118.txt","/home/dionis/mo192.168.19.110.txt","/home/dionis/mo192.168.19.92.txt","/home/dionis/mo192.168.19.83.txt","/home/dionis/mo192.168.19.200.txt","/home/dionis/mo192.168.19.183.txt","/home/dionis/mo192.168.19.23.txt","/home/dionis/mo192.168.19.135.txt","/home/dionis/mo192.168.19.111.txt","/home/dionis/mo192.168.19.227.txt","/home/dionis/mo192.168.19.151.txt","/home/dionis/mo192.168.19.179.txt","/home/dionis/mo192.168.19.10.txt","/home/dionis/mo192.168.19.120.txt","/home/dionis/mo192.168.19.46.txt"]
rutas4 = ["/home/dionis/mo192.168.4.183.txt","/home/dionis/mo192.168.4.190.txt","/home/dionis/mo192.168.4.41.txt","/home/dionis/mo192.168.4.75.txt","/home/dionis/mo192.168.4.35.txt","/home/dionis/mo192.168.4.135.txt","/home/dionis/mo192.168.4.83.txt","/home/dionis/mo192.168.4.129.txt","/home/dionis/mo192.168.4.18.txt","/home/dionis/mo192.168.4.232.txt","/home/dionis/mo192.168.4.84.txt","/home/dionis/mo192.168.4.180.txt","/home/dionis/mo192.168.4.248.txt","/home/dionis/mo192.168.4.50.txt","/home/dionis/mo192.168.4.152.txt","/home/dionis/mo192.168.4.223.txt","/home/dionis/mo192.168.4.117.txt"]
rutas5 = ["/home/dionis/mo192.168.35.176.txt","/home/dionis/mo192.168.35.170.txt","/home/dionis/mo192.168.35.65.txt","/home/dionis/mo192.168.35.71.txt","/home/dionis/mo192.168.35.127.txt","/home/dionis/mo192.168.35.16.txt","/home/dionis/mo192.168.35.133.txt","/home/dionis/mo192.168.35.69.txt","/home/dionis/mo192.168.35.34.txt","/home/dionis/mo192.168.35.9.txt","/home/dionis/mo192.168.35.213.txt","/home/dionis/mo192.168.35.135.txt","/home/dionis/mo192.168.35.20.txt"]
rutas6 = ["/home/dionis/mo192.168.4.20.txt","/home/dionis/mo192.168.4.81.txt","/home/dionis/mo192.168.4.112.txt","/home/dionis/mo192.168.4.102.txt","/home/dionis/mo192.168.4.170.txt","/home/dionis/mo192.168.4.207.txt","/home/dionis/mo192.168.4.175.txt","/home/dionis/mo192.168.4.12.txt","/home/dionis/mo192.168.4.195.txt","/home/dionis/mo192.168.4.131.txt","/home/dionis/mo192.168.4.166.txt","/home/dionis/mo192.168.4.144.txt","/home/dionis/mo192.168.4.91.txt","/home/dionis/mo192.168.4.21.txt"]
rutas7 = ["/home/dionis/mo192.168.1.210.txt","/home/dionis/mo192.168.1.35.txt","/home/dionis/mo192.168.1.63.txt","/home/dionis/mo192.168.1.211.txt","/home/dionis/mo192.168.1.166.txt","/home/dionis/mo192.168.1.149.txt","/home/dionis/mo192.168.1.122.txt","/home/dionis/mo192.168.1.171.txt","/home/dionis/mo192.168.1.173.txt","/home/dionis/mo192.168.1.126.txt","/home/dionis/mo192.168.1.123.txt","/home/dionis/mo192.168.1.96.txt","/home/dionis/mo192.168.1.56.txt","/home/dionis/mo192.168.1.172.txt","/home/dionis/mo192.168.1.65.txt","/home/dionis/mo192.168.1.145.txt","/home/dionis/mo192.168.1.152.txt","/home/dionis/mo192.168.1.32.txt","/home/dionis/mo192.168.1.140.txt","/home/dionis/mo192.168.1.19.txt"]
rutas8 = ["/home/dionis/mo192.168.9.90.txt","/home/dionis/mo192.168.9.75.txt","/home/dionis/mo192.168.9.168.txt","/home/dionis/mo192.168.9.162.txt","/home/dionis/mo192.168.9.77.txt","/home/dionis/mo192.168.9.99.txt","/home/dionis/mo192.168.9.127.txt","/home/dionis/mo192.168.9.180.txt","/home/dionis/mo192.168.9.147.txt"]
rutas9 = ["/home/dionis/mo192.168.9.198.txt","/home/dionis/mo192.168.9.116.txt","/home/dionis/mo192.168.9.46.txt","/home/dionis/mo192.168.9.120.txt","/home/dionis/mo192.168.9.166.txt","/home/dionis/mo192.168.9.60.txt","/home/dionis/mo192.168.9.95.txt","/home/dionis/mo192.168.9.130.txt","/home/dionis/mo192.168.9.66.txt"]

vector = []
vector2 = []

def nodos(ruta):
	for n in range(0, len(ruta)):
		fichero = ficheros.Fichero(ruta[n])
		texto = fichero.leer_fichero()
		linea = texto.split("\n")
		for i in range(0,len(linea)):
			if (" signal-strength:" in linea[i]):
				nivelr = linea[i]
				nivelr2 = nivelr.replace(" ","")
				nivelr3 = nivelr2.replace("signal-strength:","")
				nivelr4 = nivelr3.replace("dBm","")
				vector.append(nivelr4)
			elif(" tx-signal-strength:" in linea[i]):
				nivelt = linea[i]
				nivelt2 = nivelt.replace(" ","")
				nivelt3 = nivelt2.replace("tx-signal-strength:","")
				nivelt4 = nivelt3.replace("dBm","")
				vector.append(nivelt4)
			elif("tx-ccq:" in linea[i]):
				ccqt = linea[i]
				ccqt2 = ccqt.replace(" ","")
				ccqt3 = ccqt2.replace("tx-ccq:","")
				if ("overall" in ccqt3):
					ccqt3 = ""
				else:
					vector.append(ccqt3)
			elif("rx-ccq:" in linea[i]):
				ccqr = linea[i]
				ccqr2 = ccqr.replace(" ","")
				ccqr3 = ccqr2.replace("rx-ccq:","")
				vector.append(ccqr3)
		print(*vector,sep = ' ')
		vector.clear()
#print("cazadores")
#nodos(rutas)
#print("tierra morada")
#nodos(rutas2)
#print("manjui")
#nodos(rutas3)
#print("guadalupe")
#nodos(rutas4)
#print("bethesda")
#nodos(rutas5)
#print("santo domingo")
#nodos(rutas6)
print("pikachu")
nodos(rutas7)
print("suba2")
nodos(rutas8)
print("tibitoc")
nodos(rutas9)
