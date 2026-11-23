
def esPrimo(num):
    menor = num -1
    for x in range(2, menor):
        if num % x == 0:
            return False
    return True

print(esPrimo(5))