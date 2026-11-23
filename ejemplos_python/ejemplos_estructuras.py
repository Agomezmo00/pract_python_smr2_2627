# ============================================
# 1) SECUENCIA: instrucciones en orden
# ============================================
print("== Secuencia ==")
x, y = 10, 5
suma = x + y
print("x + y =", suma)  # 15

# ============================================
# 2) CONDICIONALES: if / elif / else
# ============================================
print("\n== Condicionales ==")
nota = 7
if nota >= 9:
    resultado = "Sobresaliente"
elif nota >= 5:
    resultado = "Aprobado"
else:
    resultado = "Suspenso"
print(f"Nota {nota} → {resultado}")

# ============================================
# 3) match-case (Python 3.10+)
# ============================================
print("\n== match-case ==")
op, a, b = "resta", 8, 3
match op:
    case "suma":
        r = a + b
    case "resta":
        r = a - b
    case "mul":
        r = a * b
    case _:
        r = "operación no soportada"
print(f"Operación '{op}' → {r}")

# ============================================
# 4) BUCLE for + continue
# ============================================
print("\n== for con continue (salta el 3) ==")
for n in range(1, 6):
    if n == 3:
        continue         # salta esta iteración
    print(n, end=" ")
print()  # salto de línea

# ============================================
# 5) for-else: se ejecuta el else si NO hubo break
#    Ejemplo típico: prueba de primalidad
# ============================================
print("\n== for-else (primos) ==")

def es_primo(n: int) -> bool:
    if n < 2:
        return False
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            # Encontramos un divisor → romper el bucle
            break
    else:
        # No hubo break: es primo
        return True
    return False

print("¿11 es primo?:", es_primo(11))  # True
print("¿12 es primo?:", es_primo(12))  # False

# ============================================
# 6) BUCLE while + else
#    El else se ejecuta cuando el while termina SIN break
# ============================================
print("\n== while + else ==")
contador = 3
while contador > 0:
    print(contador)
    contador -= 1
else:
    print("¡Despegue!")  # se ejecuta porque no hubo break

# ============================================
# 7) break en bucle: terminar antes de tiempo
# ============================================
print("\n== for con break ==")
for n in range(1, 10):
    print(n, end=" ")
    if n == 4:
        print("→ break aquí")
        break

# ============================================
# 8) pass: marcador de posición (no hace nada)
# ============================================
print("\n\n== pass (marcador) ==")
for ch in "ab c":
    if ch == " ":
        pass  # aquí podría ir lógica futura
    else:
        print(f"carácter: {ch}")