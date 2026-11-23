
bisiesto = int(input("Dime un año: "))

if bisiesto % 400 == 0:
    print("Es bisiesto")
elif bisiesto % 100 == 0:
    print("No es bisiesto")
elif bisiesto % 4 == 0:
    print("Es bisiesto")
else:
    print("No es bisiesto")