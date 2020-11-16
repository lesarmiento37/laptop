def decimalToBinary(n):  
    return bin(n).replace("0b", "")
print("ingrese")
entra = int(input())
print(decimalToBinary(entra))
