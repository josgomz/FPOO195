'''''
valor = int(input("Dame un numero: "))

for i in range(0, valor):
    if i % 2 != 0:
        print(i , end=",")
'''''
while True:        
    valor = int(input("Dame un numero entero mayor a 0: "))
    if valor > 0:
        break

for i in range(valor, 0):
    i-=1
    print(i , end=",")