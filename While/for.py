palarbra = input("Introduce una palabra: ")
for vocales in range(len(palarbra)):
    print(palarbra[vocales])

contador = 0
for vocales in palarbra:
    if vocales == "a" or vocales == "e" or vocales == "i" or vocales == "o" or vocales == "u":
        contador += 1
print("La palabra", palarbra, "tiene", contador, "vocales")

#Calcula el valor de la suma de los nimeros pares del 1 al 10
suma = 0
for i in range(1,11):
    if i % 2 == 0:
        suma += i
print("La suma de los numeros pares del 1 al 10 es:", suma)