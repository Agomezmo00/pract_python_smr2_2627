

cadena = input("Introduce una cadena de texto:\n ")

cadena = cadena.strip()
cadena = cadena.replace("  ", " ")

espacios = cadena.count(" ")
print("La cadena tiene: ", espacios+1)
listaPalabras = cadena.split(" ")
print(listaPalabras)
print("La cadena tiene: ", len(listaPalabras), " palabras")