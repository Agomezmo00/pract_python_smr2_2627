# =============================================================================
# EJERCICIO 3.3: Control de ingredientes únicos para una receta de cocina
# Estructura: dos listas de texto (ingredientes de dos platos)
# Casos límite: ingredientes repetidos dentro de una misma lista y listas sin
# ingredientes en común.
# =============================================================================

# Pareja de platos principal (con repetidos dentro de cada lista)
ingredientes_plato_1 = [
    "huevo", "patata", "cebolla", "aceite de oliva", "sal",
    "huevo",                         # repetido a propósito
    "pimienta", "ajo",
]
ingredientes_plato_2 = [
    "tomate", "cebolla", "aceite de oliva", "sal", "pan",
    "ajo", "pepino", "vinagre", "sal",   # "sal" repetida a propósito
]


def ingredientes_totales(lista1, lista2):
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    
    todo = conjunto1.union(conjunto2)
    
    return todo

todo = ingredientes_totales(ingredientes_plato_1, ingredientes_plato_2)
#print(todo)


def lista_alfabetica(lista1, lista2):
    c1 = set(lista1)
    c2 = set(lista2)
    comun = c1.intersection(c2)
    return sorted(comun)


print(lista_alfabetica(ingredientes_plato_1, ingredientes_plato_2))