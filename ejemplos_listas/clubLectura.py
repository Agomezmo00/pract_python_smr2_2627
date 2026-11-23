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



def mayoresEdad(asistentes):
    mayores = []
    for nombre, edad in asistentes:
        if edad >= 18:
            mayores.append(nombre)
    
    return mayores

listaMayores = mayoresEdad(asistentes_club_lectura)
print(listaMayores)

def buscarAsistente(lista, buscado):
    for nombre,_ in lista:
        if nombre == buscado:
            return buscado+" asistió al club de lectura"
        
    return buscado+" no asistió al club de lectura"


print(buscarAsistente(asistentes_club_lectura, "Beatriz Cano"))