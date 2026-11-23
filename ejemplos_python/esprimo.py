def esPrimo(num):
    menor = num -1
    for x in range(2, menor):
        if num % x == 0:
            return False
    return True


numero = input("Dime el número y te diré si es primo o no:\n")
print(esPrimo(int(numero)))