var = []

def lcm(a,b): 
        return(a * b / gcd(a, b))
        
def gcd(a,b): 
        while b:      
                a, b = b, a % b
        return a

entra = int(input())
for n in range(0, entra):
	a,b = input().split()
	a,b = int(a), int(b)
	mcd = gcd(a,b)
	mcm = int(lcm(a,b))
	mcd2 = "({}".format(mcd)
	mcm2 = "{})".format(mcm)
	var.append(mcd2)
	var.append(mcm2)
print(*var,sep=' ')
