class Coche:
	
	#Se crean los atributos
	def __init__(self,marca,color,combustible,cilindrada):
		self.color = color
		self.marca = marca
		self.combustible = combustible
		self.cilindrada = cilindrada
	
	def mostrar_caracteristicas(self):
		print("Este coche es de la marca {}, de color {}, de {} y una cilindrada de {}".format(self.marca,self.color,self.combustible,self.cilindrada))
coche1 = Coche("Opel","rojo","gasolina","1.6")

print(coche1.marca)
coche1.mostrar_caracteristicas()

