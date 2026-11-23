def esPar(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
for n in range(1, 100):
    if esPar(n) == True:
        print(f"{n} es par")
    else:
        print(n, " es impar")