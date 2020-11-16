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
     #print(nume2)
     if (nume2[0] < nume2[1]) and (nume2[0] < nume2[2]):
         nume3.append(nume2[0])
     elif (nume2[1] < nume2[0]) and (nume2[1] < nume2[2]):
    	  nume3.append(nume2[1])
     else:
       nume3.append(nume2[2])
     print("El resultado es:")
     print(*nume3, sep=' ')
     suma = 0  
