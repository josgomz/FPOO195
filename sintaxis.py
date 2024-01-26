#Soyy un comentario de linea
'''Soy un comentario
de varias lineas
'''
#Practica2: Sintaxis Python
#Soy un comentario
'''
soy un comentario 
de varias lineas
'''

# 2 cadenas
"""print('soy una cadena')
print('soy otra cadena')"""

a= 'mi banda favorita es \n grupo marrano'
b= 'es marrano '
# print(a+b)
# print(a,b)

# print(len(a))

# print(b[2:5])
# print(b[:5])
# print(b[2:])

# variables
# x= int(4)
# y= float(5.4)
# z= x+y
# print(x)
# print(y)
# print(z)
# print(type(x))
# print(type(y))
# print(type(z))

import random

numero= random.randrange(1,10)
print(numero)

#solicitud de datos
# var1= int(input("introduce un valor"))
# var2 = str(input("Ingrese un texto"))
# var3 = float(input("Ingrese un flotante"))
# print(var1)
# print(var2)
# print(var3)

x=1
print(x < 5 and x < 10)
print(x < 5 or x < 10)
print(not(x < 5 and x <10))