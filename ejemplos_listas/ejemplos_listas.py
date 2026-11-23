cadena = list("Tabernero hace boxeo y Luis juega al fútbol")

print(cadena.index("y"))
print(cadena.count("o"))

mayusculas = []
for l in cadena:
    mayusculas.append(l.upper())
    
print(mayusculas)