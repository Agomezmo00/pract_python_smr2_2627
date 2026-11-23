import random

notas = []

while len(notas) < 100:
    nota = random.randint(0, 10)
    notas.append(nota)

print("En mi lista tengo ", notas.count(0), " ceros.")

numCeros = notas.count(0)

'''
i = 0
while i < numCeros:
    notas.remove(0)
    i = i+1

print(len(notas), notas)
'''
# Esto lo ignora el intérprete
nuevasNotas = []
for n in notas:
    if n != 0:
        nuevasNotas.append(n)

print(len(notas))
print(len(nuevasNotas))
