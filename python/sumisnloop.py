nume2 = 0
nume3 = []

print("numero de arreglos")

num = input()
for i in range(int(num)):
     nume = input()
     nume2 = nume.split()
     suma = 0
     
     for n in range(0,len(nume2)):
	  
          nume2[n] = int(nume2[n])
          suma += int(nume2[n])
     nume3.append(suma)
     print("El resultado es:")
     print(*nume3, sep=' ')
     suma = 0  
