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
