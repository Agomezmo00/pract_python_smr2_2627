vacia = []
notas = [7, 5.25, 9, 10, 4.33, 6.75]
nombres = ["Íker", "Binxue", "Jorge",True, False, 77.543, "Erick", "Fernando", "Luis", "Adrián"]


# print(nombres[0])
# print(nombres[5])
#tam = len(nombres)
# print(tam)
# print(nombres[-1])
# print(nombres[-2])

numeros = list(range(2,501,2))
#print(numeros)
letras = list("Python")
# print(letras)
notasAlumnos = [0]*17
# print(notasAlumnos)

decenas = list(range(10,101,10))
# print(decenas[1:4])
# print(decenas[:3])
# print(decenas[::2])
# print(decenas[::-1])
# ¿Cómo se haría para mostrar los 3 últimos de mayor a menor?

print(decenas[10:6:-1])

decenas.append(110)
decenas.insert(5, 120)
docenas = list(range(12,241,12))
decenas.extend(docenas)
docenas = docenas+[252]

letras = list("Sistemas Microinformaticos y Redes")

print(letras.index("o"))
print(letras.count("o"))

print(letras)
ordenado = sorted(letras)

letras.sort()
#print(letras)

decenas.sort(reverse=True)
decenas.extend(letras)
decenas.append(True)
decenas.append(False)
#print(decenas)


for d in decenas:
    print(d)
    #print(type(d).__name__)
    if isinstance(d, bool):
        print("es booleano")
#print(ordenado)

print(type(decenas[45]).__name__)

# print(decenas)
# print(docenas)

