import random

lista = [random.randint(0, 10) for _ in range(100)]   # 100 enteros entre 0 y 10
print("0 antes:", lista.count(0))

print(lista)


sin_ceros = []
for n in lista:
    if n != 0:
        sin_ceros.append(n)

print("0 después:", lista.count(0))
print(lista)


sin_ceros = [n for n in lista if n != 0]
print("0 después:", sin_ceros.count(0), "| longitud:", len(sin_ceros))