frutas = ["Manzana", "Pera", "Uva"]
kilosComprados = [1.5, 1.00, 0.5]
precio = [2.25, 3.00, 4.25]



i = 0
while i<len(frutas):
    print("El precio de la "+frutas[i]+": ", precio[i])
    print("El importe gastado es: ", precio[i]*kilosComprados[i])
    i = i+1
    

for elem in frutas:
    print("La fruta es la: "+elem)
    
for i in range(0, len(frutas)):
    print("El importe gastado es: ", precio[i]*kilosComprados[i])
    

for n in range(0, 1000, 5):
    print(n)