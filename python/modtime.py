import math
dia1 = []
dia2 = []
var2 = []
resta = []
answer = []
def operacion(numer):
	numero = numer.split()
	sumar1 = 0
	sumar2 = 0
	print("\n")
	for n in range(0,len(numero)):
		numero[n] = int(numero[n])
		var2.append(numero[n])
	#print(var2)
	for f in range(0,4):
		dia1.append(var2[f])
	dias1(dia1)
	for g in range(4,8):
		dia2.append(var2[g])
	dias2(dia2)
	restar(resta[0],resta[1])
	print(*answer,sep = ' ')
	resta.clear()
	dia1.clear()
	dia2.clear()
	var2.clear()
	
def dias1(di1):
	suma1 = 86400*di1[0] + 3600*di1[1] + 60*di1[2] + di1[3] 
	resta.append(suma1)
	

def dias2(di2):
	suma2 = 86400*di2[0] + 3600*di2[1] + 60*di2[2] + di2[3]
	resta.append(suma2)

def restar(s1,s2):
	resta = s2 - s1	
	modulo(resta)

def modulo(rest):
	day = math.floor(rest / 86400 )
	hour = math.floor((rest % 86400) / 3600 )
	minute = math.floor((rest / 60 ) % 60)
	second = rest - day*86400 - hour*3600  - minute*60
	modu = "({} {} {} {})".format(day,hour,minute,second)
	answer.append(modu)
	 
print("ingrese")
num = int(input())
for i in range(0,num):
	nume = input()
	operacion(nume)	
