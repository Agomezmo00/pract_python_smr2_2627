listaConCosas = [44, 27.25, "Noviembre", "Jueves"]
listaDos = [False, [12, 24], {"nombre":"Antonio"}, True, 46, (33, 22)]

listaConCosas.extend(listaDos)
enteros = []
flotantes = []
textos = []
booleanos = []
otros = []

#Recorremos la listaConCosas y añadimos cada elemento a la lista que le corresponda.
for elem in listaConCosas:
    print(type(elem).__name__)