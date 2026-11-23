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
    "La Tapadera": 4.25
}

def librosAsequibles(catalogo, presupuesto):
    asequibles = []
    for titulo, precio in catalogo.items():
        if precio <= presupuesto:
            asequibles.append(titulo)
    return asequibles

print(librosAsequibles(catalogo_libreria, 9))

titulos = catalogo_libreria.keys()
print(titulos)

def existeLibroEnCatalogo(catalogo, titulo):
    return titulo in catalogo.keys()

if existeLibroEnCatalogo(catalogo_libreria, "La Tapadera"):
    print("La Tapadera está en el catálogo")
else:
    print("La Tapadera no está en el catálogo")
    
def consultar_precio(catalogo, titulo):
    if existeLibroEnCatalogo(catalogo, titulo):
        precio = catalogo.get(titulo)
        return f"'{titulo}' cuesta {precio} "
    else:
        return f"El libro '{titulo}' no está en el catálogo"

print(consultar_precio(catalogo_libreria, "Bodas de sangre"))
print(consultar_precio(catalogo_libreria, "Matar a un ruiseñor"))

def precioMedio(catalogo):
    return sum(catalogo.values())/len(catalogo)

print("El precio medio del catálogo es: ", round(precioMedio(catalogo_libreria),2))