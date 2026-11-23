
def esBisiesto(bisiesto):
    if bisiesto % 400 == 0:
        return True
    elif bisiesto % 4 == 0 and bisiesto % 100 != 0:
        return True
    else:
        return False
    


juanito = int(input("Dime un año: "))

if esBisiesto(juanito) == True:
    print(f"El año {juanito} es bisiesto.")
else:
    print(f"El año {juanito} no es bisiesto.")