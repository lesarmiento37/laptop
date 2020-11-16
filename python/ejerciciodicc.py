diccionario_frutas = {"manzana":"apple" , "naranja":"orange" , "platano":"banana" , "limon":"lemon"}
print(diccionario_frutas["naranja"])
diccionario_frutas["piña"] = "pinneapple"
for clave,valor in diccionario_frutas.items():
    print(clave,valor)
