"""
Datos de prueba para los ejercicios de Python.

Contiene las estructuras de datos descritas en los enunciados, organizadas en
dos bloques:

  BLOQUE A: ejercicios básicos      (1.1, 2.2, 3.3 y 4.4)
  BLOQUE B: ejercicios intermedios  (1, 2, 3 y 4)

Cada variable lleva un comentario con el ejercicio al que pertenece. Los datos
incluyen casos "normales" y también casos límite (valores en el borde de una
condición, entradas inválidas, estructuras vacías...) para poder probar bien
las soluciones.

Uso:
    from datos_ejercicios import asistentes_club_lectura, catalogo_libreria
"""


# #############################################################################
# BLOQUE A: EJERCICIOS BÁSICOS
# #############################################################################


# =============================================================================
# EJERCICIO 1.1: Registro de participantes en un taller de lectura
# Estructura: lista de tuplas (nombre_asistente, edad)
# Casos límite: edades justo en 17 y 18, y una lista vacía.
# =============================================================================

asistentes_club_lectura = [
    ("Lucía Fernández", 34),
    ("Pablo Ortega", 16),
    ("Marta Romero", 18),      # límite: justo mayor de edad
    ("Iván Castro", 12),
    ("Elena Vidal", 67),
    ("Javier Molina", 17),     # límite: un año menos
    ("Carmen Ruiz", 45),
    ("Alberto Gil", 29),
    ("Sofía Navarro", 15),
    ("Diego Herrera", 52),
    ("Paula Serrano", 19),
    ("Raúl Domínguez", 71),
    ("Nuria Campos", 14),
    ("Andrés Peña", 38),
    ("Laura Iglesias", 23),
    ("Hugo Santos", 11),
    ("Isabel Moreno", 60),
    ("Sergio Vargas", 18),      # límite: justo mayor de edad
    ("Rocío Delgado", 41),
    ("Tomás Aguilar", 16),
    ("Beatriz Cano", 27),
    ("Ángel Prieto", 83),
    ("Claudia Marín", 13),
    ("Fernando Soto", 35),
]

# Lista vacía: ¿qué debe devolver cada función si nadie ha asistido?
asistentes_club_lectura_vacio = []

# Nombres para probar la función de búsqueda (los tres primeros asistieron)
nombres_a_buscar_club = [
    "Marta Romero",
    "Ángel Prieto",
    "Iván Castro",             # asistió, pero es menor de edad
    "Carlos Jiménez",          # no asistió
    "marta romero",            # mismo nombre en minúsculas: ¿lo encuentra?
    "",                        # cadena vacía
]


# =============================================================================
# EJERCICIO 2.2: Catálogo y búsqueda rápida en una pequeña librería
# Estructura: diccionario {título_del_libro: precio_en_euros}
# Casos límite: libros con precios redondos (5.00, 10.00) para probar "<=".
# =============================================================================

catalogo_libreria = {
    "Don Quijote de la Mancha": 12.50,
    "La sombra del viento": 8.90,
    "Cien años de soledad": 10.00,   # límite con presupuesto de 10
    "Rayuela": 15.75,
    "El nombre de la rosa": 9.95,
    "Pedro Páramo": 5.00,            # límite con presupuesto de 5
    "La casa de los espíritus": 11.30,
    "Crónica de una muerte anunciada": 6.50,
    "Los renglones torcidos de Dios": 13.20,
    "El túnel": 4.75,
    "La ciudad y los perros": 9.00,
    "Fortunata y Jacinta": 18.90,
    "Niebla": 7.40,
    "El Aleph": 8.25,
    "Platero y yo": 3.99,
    "La Regenta": 16.00,
    "Marianela": 5.50,
    "Bodas de sangre": 4.20,
    "El árbol de la ciencia": 7.80,
    "Tiempo de silencio": 8.60,
}

# Presupuestos para probar la función de filtrado (incluye casos extremos)
presupuestos_libreria = [0, 3.99, 5, 10, 12.50, 20, 100]

# Títulos para probar la consulta de precio (algunos no existen)
titulos_a_consultar_libreria = [
    "Rayuela",
    "Platero y yo",
    "Ulises",                        # no existe
    "rayuela",                       # existe, pero con otra capitalización
    "El Aleph",
    "",                              # cadena vacía
]

# Catálogo vacío para probar casos límite
catalogo_libreria_vacio = {}


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

# Pareja sin ingredientes en común (la intersección debe quedar vacía)
ingredientes_plato_sin_comunes_1 = ["chocolate", "nata", "azúcar", "harina"]
ingredientes_plato_sin_comunes_2 = ["merluza", "limón", "perejil", "patata"]

# Pareja con listas idénticas (la unión y la intersección coinciden)
ingredientes_plato_identicos = ["arroz", "agua", "sal", "aceite de oliva"]

# Lista vacía para probar casos límite
ingredientes_plato_vacio = []

# Recetas de la semana: sirven para formar tantas parejas como quieras
# (por ejemplo: recetas_semana["Lunes"] y recetas_semana["Martes"])
recetas_semana = {
    "Lunes": ["lentejas", "chorizo", "zanahoria", "cebolla", "ajo", "aceite de oliva", "sal", "laurel"],
    "Martes": ["merluza", "patata", "limón", "perejil", "ajo", "aceite de oliva", "sal"],
    "Miércoles": ["arroz", "pollo", "pimiento rojo", "tomate", "cebolla", "ajo", "aceite de oliva", "sal", "azafrán"],
    "Jueves": ["espaguetis", "tomate", "albahaca", "ajo", "aceite de oliva", "sal", "queso parmesano"],
    "Viernes": ["huevo", "patata", "cebolla", "aceite de oliva", "sal"],
    "Sábado": ["harina", "huevo", "leche", "azúcar", "mantequilla", "sal", "levadura"],
    "Domingo": ["cordero", "patata", "ajo", "romero", "aceite de oliva", "sal", "vino blanco"],
}


# =============================================================================
# EJERCICIO 4.4: Resumen de puntos en una partida de juegos de mesa
# Estructura: lista de tuplas (nombre_jugador, puntos_obtenidos)
# Un jugador aparece varias veces (una por ronda).
# =============================================================================

# Partida con un único ganador claro (Marta: 69 puntos)
rondas_partida = [
    ("Ana", 10), ("Luis", 7), ("Marta", 12), ("Pedro", 5), ("Lola", 9),
    ("Ana", 5), ("Luis", 9), ("Marta", 14), ("Pedro", 11), ("Lola", 6),
    ("Ana", 8), ("Luis", 6), ("Marta", 8), ("Pedro", 7), ("Lola", 12),
    ("Ana", 12), ("Luis", 10), ("Marta", 15), ("Pedro", 9), ("Lola", 4),
    ("Ana", 7), ("Luis", 8), ("Marta", 10), ("Pedro", 6), ("Lola", 10),
    ("Ana", 9), ("Luis", 5), ("Marta", 10),
]

# Partida con EMPATE en cabeza (Ana y Luis suman lo mismo)
rondas_partida_empate = [
    ("Ana", 10), ("Luis", 12), ("Marta", 5),
    ("Ana", 15), ("Luis", 13), ("Marta", 8),
    ("Ana", 5), ("Luis", 5), ("Marta", 6),
]

# Partida donde cada jugador juega una sola ronda
rondas_partida_una_ronda = [("Ana", 20), ("Luis", 35), ("Marta", 15)]

# Partida con puntuaciones negativas (penalizaciones)
rondas_partida_con_penalizaciones = [
    ("Ana", 10), ("Luis", -5), ("Marta", 7),
    ("Ana", -3), ("Luis", 8), ("Marta", -10),
    ("Ana", 6), ("Luis", 4), ("Marta", 2),
]

# Lista vacía para probar casos límite
rondas_partida_vacia = []


# #############################################################################
# BLOQUE B: EJERCICIOS INTERMEDIOS
# #############################################################################


# =============================================================================
# EJERCICIO 1 (intermedio): Gestión de inventario y alertas de stock
# Estructura: diccionario {producto: (precio_unitario, cantidad_en_stock)}
#             y lista de ventas [(producto, cantidad_vendida), ...]
# Umbral de stock crítico: 3 unidades o menos.
# =============================================================================

inventario_tienda = {
    "leche":            (1.20, 25),
    "pan":              (0.80, 5),
    "huevos":           (2.50, 4),    # justo por encima del umbral crítico
    "aceite":           (6.90, 2),    # ya crítico
    "arroz":            (1.10, 30),
    "azúcar":           (1.05, 12),
    "harina":           (0.95, 3),    # exactamente en el umbral (3)
    "pasta":            (1.30, 18),
    "tomate frito":     (1.60, 9),
    "atún en lata":     (1.75, 14),
    "café":             (3.20, 6),
    "galletas":         (1.90, 8),
    "yogur":            (0.55, 40),
    "queso":            (4.80, 3),    # exactamente en el umbral (3)
    "jamón":            (9.50, 1),    # crítico
    "zumo de naranja":  (1.45, 0),    # agotado
}

# Ventas del día: incluye situaciones problemáticas a propósito
ventas_del_dia = [
    ("leche", 6),
    ("pan", 2),
    ("huevos", 3),
    ("aceite", 1),
    ("arroz", 10),
    ("pan", 4),                       # junto con la venta anterior, supera el stock del pan
    ("café", 2),
    ("galletas", 3),
    ("yogur", 12),
    ("jamón", 1),
    ("zumo de naranja", 1),           # producto agotado
    ("vino tinto", 1),                # producto que no existe en el inventario
    ("queso", 0),                     # cantidad cero
    ("atún en lata", -2),             # cantidad negativa
    ("pasta", 5),
    ("harina", 4),                    # intenta vender más de lo que hay
]

# Ventas sin ningún problema (para comprobar el caso feliz)
ventas_del_dia_validas = [
    ("leche", 5), ("pan", 1), ("arroz", 4), ("yogur", 8), ("café", 1),
]

# Lista de ventas vacía
ventas_del_dia_vacia = []

# Inventario vacío
inventario_tienda_vacio = {}


# =============================================================================
# EJERCICIO 2 (intermedio): Análisis y solapamiento de rutas de reparto
# Estructura: diccionario {repartidor: [códigos_postales_visitados_cada_día]}
# Las zonas se repiten a lo largo de la semana (por eso se usan sets).
# =============================================================================

# Caso principal: dos repartidores, como en el enunciado
rutas_reparto = {
    "Carlos": ["41001", "41002", "41003", "41001", "41005", "41002", "41007", "41001", "41003", "41008"],
    "Marta":  ["41002", "41004", "41005", "41004", "41006", "41005", "41009", "41004", "41002", "41010"],
}

# Zonas prioritarias obligatorias: cada repartidor cubre al menos una, pero no todas
zonas_prioritarias = ["41001", "41005", "41008"]

# Zonas prioritarias que NADIE visita (la validación debe fallar)
zonas_prioritarias_sin_cubrir = ["41099", "41098"]

# Zonas prioritarias que ambos cubren por completo (la validación estricta debe pasar)
zonas_prioritarias_cubiertas = ["41002", "41005"]

# Zonas prioritarias que solo cubre uno de los dos repartidores
zonas_prioritarias_desiguales = ["41001", "41003", "41007", "41008"]

# Caso ampliado: tres repartidores (para probar que la solución generaliza)
rutas_reparto_tres = {
    "Carlos": ["41001", "41002", "41003", "41001", "41005"],
    "Marta":  ["41002", "41004", "41005", "41004", "41006"],
    "Sergio": ["41005", "41006", "41011", "41012", "41001"],
}

# Rutas idénticas: no hay ninguna zona exclusiva
rutas_reparto_identicas = {
    "Carlos": ["41001", "41002", "41003"],
    "Marta":  ["41003", "41002", "41001"],
}

# Rutas totalmente disjuntas: todas las zonas son exclusivas
rutas_reparto_disjuntas = {
    "Carlos": ["41001", "41002", "41003", "41001"],
    "Marta":  ["41004", "41005", "41006", "41004"],
}

# Un repartidor sin visitas
rutas_reparto_con_vacio = {
    "Carlos": ["41001", "41002", "41003"],
    "Marta":  [],
}


# =============================================================================
# EJERCICIO 3 (intermedio): Procesamiento y filtrado de valoraciones
# Estructura: lista de diccionarios
#             {"plato": str, "puntuacion": int, "comentario": str}
# Incluye entradas inválidas: puntuación fuera de rango (1-5), plato vacío,
# tipos incorrectos y claves ausentes.
# =============================================================================

valoraciones_brutas = [
    # --- Paella: muy bien valorada (debería ser "Plato Estrella") ---
    {"plato": "Paella", "puntuacion": 5, "comentario": "Excelente, arroz en su punto"},
    {"plato": "paella ", "puntuacion": 4, "comentario": "Muy buena (con un espacio sobrante)"},
    {"plato": "PAELLA", "puntuacion": 5, "comentario": "Perfecta"},
    {"plato": "Paella", "puntuacion": 5, "comentario": "La mejor que he probado"},
    {"plato": "Paella", "puntuacion": 4, "comentario": "Muy rica"},

    # --- Croquetas: también estrella ---
    {"plato": "Croquetas", "puntuacion": 5, "comentario": "Caseras y cremosas"},
    {"plato": "Croquetas", "puntuacion": 5, "comentario": "Geniales"},
    {"plato": "Croquetas", "puntuacion": 4, "comentario": "Muy ricas"},
    {"plato": "croquetas", "puntuacion": 5, "comentario": "Repetiría"},

    # --- Gazpacho: media baja (debería ser "Plato a Revisar") ---
    {"plato": "Gazpacho", "puntuacion": 3, "comentario": "Normal"},
    {"plato": "Gazpacho", "puntuacion": 2, "comentario": "Algo soso"},
    {"plato": "Gazpacho", "puntuacion": 3, "comentario": "Demasiado ácido"},
    {"plato": " Gazpacho", "puntuacion": 2, "comentario": "Poco frío"},

    # --- Flan: buena media pero pocas reseñas (ni estrella ni a revisar) ---
    {"plato": "Flan", "puntuacion": 4, "comentario": "Bueno"},
    {"plato": "Flan", "puntuacion": 4, "comentario": "Casero"},

    # --- Salmorejo: media alta con solo 2 reseñas (no llega a estrella) ---
    {"plato": "Salmorejo", "puntuacion": 5, "comentario": "Espectacular"},
    {"plato": "Salmorejo", "puntuacion": 5, "comentario": "Muy cremoso"},

    # --- Pulpo: media intermedia (3.5 a 4.2), sin categoría ---
    {"plato": "Pulpo", "puntuacion": 4, "comentario": "Tierno"},
    {"plato": "Pulpo", "puntuacion": 4, "comentario": "Bien cocido"},
    {"plato": "Pulpo", "puntuacion": 3, "comentario": "Algo duro"},
    {"plato": "Pulpo", "puntuacion": 4, "comentario": "Rico"},

    # --- Tarta de queso: media justo en 4.2 con 5 reseñas (límite de estrella) ---
    {"plato": "Tarta de queso", "puntuacion": 5, "comentario": "Increíble"},
    {"plato": "Tarta de queso", "puntuacion": 4, "comentario": "Muy buena"},
    {"plato": "Tarta de queso", "puntuacion": 4, "comentario": "Buena"},
    {"plato": "Tarta de queso", "puntuacion": 4, "comentario": "Cremosa"},
    {"plato": "Tarta de queso", "puntuacion": 4, "comentario": "Rica"},

    # --- Entradas INVÁLIDAS (deben descartarse en la limpieza) ---
    {"plato": "Tortilla", "puntuacion": 7, "comentario": "Puntuación por encima del rango"},
    {"plato": "Tortilla", "puntuacion": 0, "comentario": "Puntuación por debajo del rango"},
    {"plato": "Tortilla", "puntuacion": -3, "comentario": "Puntuación negativa"},
    {"plato": "", "puntuacion": 5, "comentario": "Nombre de plato vacío"},
    {"plato": "   ", "puntuacion": 4, "comentario": "Nombre de plato solo con espacios"},
    {"plato": "Sopa", "puntuacion": "5", "comentario": "Puntuación como texto"},
    {"plato": "Sopa", "puntuacion": 4.5, "comentario": "Puntuación decimal"},
    {"plato": "Sopa", "puntuacion": None, "comentario": "Puntuación nula"},
    {"plato": "Sopa", "puntuacion": True, "comentario": "Booleano disfrazado de puntuación"},
    {"plato": None, "puntuacion": 3, "comentario": "Plato nulo"},
    {"puntuacion": 3, "comentario": "Falta la clave 'plato'"},
    {"plato": "Ensalada", "comentario": "Falta la clave 'puntuacion'"},

    # --- Entrada válida sin comentario (la clave 'comentario' es opcional) ---
    {"plato": "Ensalada", "puntuacion": 3},
]

# Todas las entradas son válidas (la limpieza no debe descartar nada)
valoraciones_validas = [
    {"plato": "Paella", "puntuacion": 5, "comentario": "Genial"},
    {"plato": "Paella", "puntuacion": 4, "comentario": "Muy buena"},
    {"plato": "Flan", "puntuacion": 3, "comentario": "Normal"},
]

# Todas las entradas son inválidas (tras la limpieza debe quedar vacía)
valoraciones_invalidas = [
    {"plato": "", "puntuacion": 3, "comentario": "Sin plato"},
    {"plato": "Paella", "puntuacion": 9, "comentario": "Fuera de rango"},
    {"plato": "Flan", "puntuacion": 0, "comentario": "Fuera de rango"},
]

# Lista vacía
valoraciones_vacias = []


# =============================================================================
# EJERCICIO 4 (intermedio): Planificador y validación de turnos en una cafetería
# Estructura: diccionario {día: [(nombre_empleado, turno), ...]}
# Turnos válidos: "Mañana" o "Tarde". Días: Lunes a Viernes.
# =============================================================================

# Semana con varios incumplimientos: Martes (falta Tarde), Miércoles (falta
# Mañana) y Viernes (sin personal). "Pedro" solo aparece con un turno no válido.
turnos_semana = {
    "Lunes": [("Ana", "Mañana"), ("Luis", "Tarde"), ("Marta", "Tarde")],
    "Martes": [("Ana", "Mañana"), ("Marta", "Mañana"), ("Sergio", "Mañana")],
    "Miércoles": [("Luis", "Tarde"), ("Marta", "Tarde")],
    "Jueves": [("Pedro", "Descanso"), ("Ana", "Mañana"), ("Marta", "Tarde")],
    "Viernes": [],
}

# Semana en la que se cumple la normativa todos los días
turnos_semana_correcto = {
    "Lunes": [("Ana", "Mañana"), ("Luis", "Tarde")],
    "Martes": [("Marta", "Mañana"), ("Sergio", "Tarde"), ("Ana", "Tarde")],
    "Miércoles": [("Ana", "Mañana"), ("Luis", "Mañana"), ("Marta", "Tarde")],
    "Jueves": [("Sergio", "Mañana"), ("Luis", "Tarde")],
    "Viernes": [("Marta", "Mañana"), ("Ana", "Tarde"), ("Pedro", "Tarde")],
}

# Semana en la que nadie cumple la normativa (todos los días incumplen)
turnos_semana_todo_mal = {
    "Lunes": [("Ana", "Mañana")],
    "Martes": [("Luis", "Tarde")],
    "Miércoles": [],
    "Jueves": [("Marta", "Mañana"), ("Sergio", "Mañana")],
    "Viernes": [("Pedro", "Tarde"), ("Ana", "Tarde")],
}

# Semana incompleta: faltan días en el diccionario (Martes y Jueves)
turnos_semana_incompleto = {
    "Lunes": [("Ana", "Mañana"), ("Luis", "Tarde")],
    "Miércoles": [("Marta", "Mañana"), ("Sergio", "Tarde")],
    "Viernes": [("Ana", "Mañana"), ("Pedro", "Tarde")],
}

# Semana con turnos mal escritos (probar la robustez ante datos sucios)
turnos_semana_turnos_raros = {
    "Lunes": [("Ana", "mañana"), ("Luis", "TARDE")],                # distinta capitalización
    "Martes": [("Marta", "Noche"), ("Sergio", "Mañana"), ("Ana", "Tarde")],
    "Miércoles": [("Luis", ""), ("Pedro", "Tarde")],
    "Jueves": [("Ana", "Mañana"), ("Marta", "Tarde")],
    "Viernes": [("Sergio", "Mañana"), ("Luis", "Tarde")],
}

# Diccionario vacío
turnos_semana_vacio = {}


# =============================================================================
# Comprobación rápida: al ejecutar este fichero se muestra un resumen de los
# datos disponibles para cada ejercicio.
# =============================================================================

if __name__ == "__main__":
    print("BLOQUE A: ejercicios básicos")
    print(f"  1.1  asistentes_club_lectura: {len(asistentes_club_lectura)} asistentes")
    print(f"  2.2  catalogo_libreria:       {len(catalogo_libreria)} libros")
    print(f"  3.3  ingredientes:            {len(ingredientes_plato_1)} y {len(ingredientes_plato_2)} elementos, "
          f"{len(recetas_semana)} recetas de la semana")
    print(f"  4.4  rondas_partida:          {len(rondas_partida)} anotaciones")

    print("\nBLOQUE B: ejercicios intermedios")
    print(f"  Ej.1 inventario_tienda:       {len(inventario_tienda)} productos, "
          f"{len(ventas_del_dia)} ventas")
    print(f"  Ej.2 rutas_reparto:           {len(rutas_reparto)} repartidores, "
          f"{len(zonas_prioritarias)} zonas prioritarias")
    print(f"  Ej.3 valoraciones_brutas:     {len(valoraciones_brutas)} entradas")
    print(f"  Ej.4 turnos_semana:           {len(turnos_semana)} días")