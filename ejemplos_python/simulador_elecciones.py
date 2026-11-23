def simular_reparto_dhondt(votos_partidos, escanos_totales, votos_en_blanco=0):
    """
    Simula el reparto de escaños de una circunscripción según el sistema D'Hondt
    regulado en el artículo 163 de la LOREG (España).

    Parámetros:
    - votos_partidos (dict): Diccionario con formato {'Nombre_Partido': int_votos}.
    - escanos_totales (int): Número total de diputados a repartir en la circunscripción.
    - votos_en_blanco (int): Votos en blanco emitidos (cuentan para el cálculo del 3%).

    Retorna:
    - dict: Diccionario con los escaños asignados a cada candidatura.
    """
    # 1. Cálculo de votos válidos totales
    # En España, el porcentaje de barrera electoral se calcula sobre los "votos válidos",
    # que incluyen la suma de votos a candidaturas más los votos en blanco (los nulos no cuentan).
    votos_candidaturas = sum(votos_partidos.values())
    votos_validos = votos_candidaturas + votos_en_blanco

    if votos_validos == 0 or escanos_totales <= 0:
        return {partido: 0 for partido in votos_partidos}

    # 2. Aplicación de la barrera electoral del 3 % (Art. 163.1.a LOREG)
    # Se excluyen del reparto las candidaturas que no alcancen al menos el 3 %
    # de los votos válidos emitidos en la circunscripción.
    umbral_minimo = votos_validos * 0.03
    partidos_aptos = {
        partido: votos
        for partido, votos in votos_partidos.items()
        if votos >= umbral_minimo
    }

    # Inicializamos el diccionario de resultados con 0 escaños para todos los partidos
    escanos_asignados = {partido: 0 for partido in votos_partidos}

    # Si ningún partido supera la barrera (caso extremo teórico), no se reparten escaños
    if not partidos_aptos:
        return escanos_asignados

    # 3. Construcción de la tabla de cocientes D'Hondt (Art. 163.1.b LOREG)
    # Se divide el número de votos obtenidos por cada candidatura por 1, 2, 3...
    # hasta un número igual al de escaños correspondientes a la circunscripción.
    tabla_cocientes = []
    for partido, votos in partidos_aptos.items():
        for divisor in range(1, escanos_totales + 1):
            cociente = votos / divisor
            # Guardamos una tupla con:
            # (cociente, votos_totales_partido, nombre_partido)
            # Incluir votos_totales_partido permite resolver empates de cociente
            # directamente al ordenar, ya que la ley otorga el escaño al partido con más votos.
            tabla_cocientes.append((cociente, votos, partido))

    # 4. Ordenación de los cocientes de mayor a menor (Art. 163.1.c LOREG)
    # Python ordena tuplas elemento a elemento: primero por 'cociente' (descendente)
    # y, en caso de empate exacto en el cociente, por 'votos' totales (descendente).
    tabla_cocientes.sort(key=lambda x: (x[0], x[1]), reverse=True)

    # 5. Asignación de los escaños (Art. 163.1.c y 163.1.d LOREG)
    # Se seleccionan los N primeros cocientes más altos, donde N = escanos_totales.
    # Nota: Si persistiera el empate tanto en cociente como en votos totales,
    # la LOREG establece que el primer empate se resuelve por sorteo y los sucesivos
    # de forma alternativa.
    ganadores = tabla_cocientes[:escanos_totales]

    for _, _, partido in ganadores:
        escanos_asignados[partido] += 1

    return escanos_asignados


# --- EJEMPLO DE USO ---
if __name__ == "__main__":
    # Supongamos una circunscripción ficticia con 7 escaños en juego
    escanos_circunscripcion = 7
    votos_blanco = 1500
    resultados_urna = {
        "Partido A": 120000,
        "Partido B": 85000,
        "Partido C": 42000,
        "Partido D": 18000,
        "Partido E": 5000,  # No superará el 3 % de los votos válidos
    }

    reparto = simular_reparto_dhondt(
        votos_partidos=resultados_urna,
        escanos_totales=escanos_circunscripcion,
        votos_en_blanco=votos_blanco,
    )

    print(f"Total votos válidos: {sum(resultados_urna.values()) + votos_blanco}")
    print(f"Umbral del 3%: {(sum(resultados_urna.values()) + votos_blanco) * 0.03:.2f} votos\n")
    print("Resultado del reparto de diputados:")
    for partido, diputados in reparto.items():
        print(f"  - {partido}: {diputados} escaños")