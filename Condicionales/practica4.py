#Pets 1
contrasoli = str(input("Insert a password: "))
contrarep = str(input("Insert the password again:"))

if contrasoli == contrarep:
    print("Correct password")
else: 
    print("Incorrect password")
    
#Pets 2
z = int(input("Ingresa un valor par"))
if z % 2 == 0:
    print(z, "es impar")
else:
    print(z, "no es par")
    
#Pets 3
edad = int(input("Ingresa tu edad: "))

if edad <= 4:
    print("Pasale chamaco oasas de a grapa")
elif edad > 4 and edad > 18:
    print("Pasale pero pagame $110")
    input("Paga:): ")
else:
    print("Pasale pero pagas $190")
    input("Pagame:): ")
    
# Pets 4
cadena1 = input("Ingrese una cadena de caracteres: ")

# Verificar si la cadena y su inversa son iguales
if cadena1 == cadena1[::-1]:
    print(cadena1, "es un palindromo")
else:
    print(cadena1, "no es un palindromo")
