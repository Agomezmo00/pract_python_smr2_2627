notas = [5.25, 6, 7, 2.25, 8.33, 9, 10, 1.33]


# min, max, sum, len --> Mostrar, nota más alta, más baja, nota media.
# all, any --> mostrar si hay algún suspenso, si no hay ningún cero.  

print("¿Cuántas notas hay? -->", len(notas))
print("Nota más alta: ", max(notas))
print("Nota más baja: ", min(notas))
print("Nota media: ", sum(notas)/len(notas))
print("Hay suspensos? ", any(notas)<5)
print("Hay algún cero?", all(notas)==0)
