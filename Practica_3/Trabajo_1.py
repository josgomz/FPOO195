#Codigo 1
#x = float(input("Ingresa tus horas trabajadas: "))
#y = float(input("Ingresa el pago por hora: "))
#z = x*y
#print(z)

#Codigo 2

#nombre = str(input("Ingresa tu nombre completo: "))
#print(nombre.lower())
#print(nombre.upper())
#print(nombre.capitalize())



#Codigo 3
#'''''
# Solicitar un entero X al usuario
X = int(input("Ingrese un entero X: "))
# Calcular la suma de los enteros desde 1 hasta X
suma = sum(range(1, X + 1))
print(suma)
#'''''

#Codigo 4
# Solicitar el nombre del usuario
nombre = input("Ingrese su nombre: ")

# Contar el número de letras en el nombre
num_letras = len(nombre)

# Mostrar el resultado
print("Tiene", num_letras)


#Codigo 5

# Solicitar el número de payasos y muñecas vendidos
num_payasos = int(input("Ingrese el número de payasos vendidos: "))
num_muñecas = int(input("Ingrese el número de muñecas vendidas: "))

# Definir pesos de payaso y muñeca
peso_payaso = 112  # g
peso_muñeca = 75   # g

# Calcular el peso total del paquete
peso_total = num_payasos * peso_payaso + num_muñecas * peso_muñeca

# Mostrar el resultado
print(peso_total, "g")

#Codigo 6

# Solicitar al usuario que introduzca una frase
frase = input("Ingrese una frase: ")

# Invertir la frase
print(frase[::-1])