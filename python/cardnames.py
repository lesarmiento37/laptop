import numpy as np
import math
var = []
print("ingrese")
suits = ['Clubs', 'Spades', 'Diamonds', 'Hearts']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
entra = int(input())
entrada = input().split()
entrada2 = np.array(entrada, dtype = int)
for n in range(0,entra):
	suit_value = int(math.floor(entrada2[n] / 13))
	rank_value = entrada2[n] % 13
	salida = "{}-of-{}".format(ranks[rank_value],suits[suit_value])
	var.append(salida)
print(*var,sep=' ')


