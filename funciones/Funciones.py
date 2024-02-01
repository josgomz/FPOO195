'''''
def IVA(cantidad_sin_iva, porcentaje_iva=None):
    # Establecer el porcentaje de IVA predeterminado si no se proporciona
    if porcentaje_iva is None:
        porcentaje_iva = 21  # Porcentaje de IVA por defecto

    # Calcular el total de la factura
    total_factura = cantidad_sin_iva + (cantidad_sin_iva * porcentaje_iva / 100)

    return total_factura

# Ejemplos de uso:
iva = int(input("Ingresa 0 si no tienes iva o 1 si tienes iva: "))
if iva == 0:
    cantidad_sin_iva_1 = float(input("Ingresa tu factura: "))
    total_factura_1 = IVA(cantidad_sin_iva_1)
    print(f"Total de la factura: {total_factura_1} con iva incluido")
else:
    cantidad_sin_iva_2 = float(input("Ingresa tu factura: "))
    porcentaje_iva_2 = float(input("Ingresa el iva: "))
    total_factura_2 = IVA(cantidad_sin_iva_2, porcentaje_iva_2)
    print(f"Total de la factura 2: {total_factura_2} con iva incluido")
'''''
'''''
import math

def calcular_area_circulo(radio):
    # Calcular el área de un círculo usando la fórmula A = π * r^2
    area = math.pi * radio**2
    return area

def calcular_volumen_cilindro(radio, altura):
    # Calcular el volumen de un cilindro usando la función anterior y la fórmula V = A * h
    area_base = calcular_area_circulo(radio)
    volumen = area_base * altura
    return volumen

# Ejemplos de uso:
radio_circulo = float(input("Ingresa el radio: "))
area_circulo = calcular_area_circulo(radio_circulo)
print(f"Área del círculo con radio {radio_circulo}: {area_circulo}")

radio_cilindro = float(input("Ingresa el radio: "))
altura_cilindro = float(input("Ingresa la altua: "))
volumen_cilindro = calcular_volumen_cilindro(radio_cilindro, altura_cilindro)
print(f"Volumen del cilindro con radio {radio_cilindro} y altura {altura_cilindro}: {volumen_cilindro}")
'''''

def decimal_a_binario(decimal):
    # Convierte un número decimal a binario utilizando la función bin()
    binario = bin(decimal)[2:]  # Se eliminan los dos primeros caracteres '0b'
    return binario

def binario_a_decimal(binario):
    # Convierte un número binario a decimal utilizando la función int() con base 2
    decimal = int(binario, 2)
    return decimal

# Ejemplos de uso:
numero_decimal = int(input("Ingresa un numero en decimal: "))
numero_binario = decimal_a_binario(numero_decimal)
print(f"{numero_decimal} en binario es: {numero_binario}")

numero_binario = str(input("Ingresa tu factura: "))
numero_decimal = binario_a_decimal(numero_binario)
print(f"{numero_binario} en decimal es: {numero_decimal}")

