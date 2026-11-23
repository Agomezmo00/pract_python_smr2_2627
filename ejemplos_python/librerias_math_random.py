import math
import random


radio = 3
area = math.pi*3*3
area_redondeada = round(area, 2)
print("El área del círculo es: ", area_redondeada)

aleatorio = random.randint(1, 20)
print(aleatorio)


def long_circunferencia(radio):
    return radio * 2 * math.pi

resultado = long_circunferencia(17)

print("La longitud de la circunferencia es: ",resultado)

contador = 1
while contador <= 100:
    print("La longitud de la circunferencia es: ", long_circunferencia(contador))
    contador = contador+1
    
embarazada = True

print(type(contador))
print(type(area))
print(type(embarazada))