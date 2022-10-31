import random as r
def generarTablero():
    tamano = r.randint(8,10)
    matriz = []
    for i in range(0, tamano):
        matriz.append([[]*tamano]*tamano)
    totalCasillas = pow(tamano,2)
    ganarCincoPuntos = int(totalCasillas*0.3)
    ganarDiezPuntos = int(totalCasillas*0.15)
    perderCincoPuntos = int(totalCasillas*0.3)
    perderDiezPuntos = int(totalCasillas*0.15)
    restantes = totalCasillas-ganarCincoPuntos-ganarDiezPuntos-perderCincoPuntos-perderDiezPuntos
    print(f"Total de casillas: {totalCasillas}\nGanar cinco puntos: {ganarCincoPuntos}\nGanar diez puntos: {ganarDiezPuntos}\
            \nPerderCincoPuntos: {perderCincoPuntos}\nPerderDiezPuntos: {perderDiezPuntos}\nRestantes: {restantes}")
    contador = 0
    while True:
        if contador == ganarCincoPuntos:
            contador = 0
            break
        fila = r.randint(0,tamano-1)
        columna = r.randint(0, tamano-1)
        if not isinstance(matriz[fila][columna], int):
            matriz[fila][columna] = 5
            contador += 1
    while True:
        if contador == ganarDiezPuntos:
            contador = 0
            break
        fila = r.randint(0,tamano-1)
        columna = r.randint(0, tamano-1)
        if not isinstance(matriz[fila][columna], int):
            matriz[fila][columna] = 10
            contador += 1
    while True:
        if contador == perderCincoPuntos:
            contador = 0
            break
        fila = r.randint(0,tamano-1)
        columna = r.randint(0, tamano-1)
        if not isinstance(matriz[fila][columna], int):
            matriz[fila][columna] = -5
            contador += 1
    while True:
        if contador == perderDiezPuntos:
            contador = 0
            break
        fila = r.randint(0,tamano-1)
        columna = r.randint(0, tamano-1)
        if not isinstance(matriz[fila][columna], int):
            matriz[fila][columna] = -10
            contador += 1
    while True:
        if contador == restantes-2:
            break
        fila = r.randint(0,tamano-1)
        columna = r.randint(0, tamano-1)
        if not isinstance(matriz[fila][columna], int):
            matriz[fila][columna] = 0
            contador += 1
    while True:
        filaGanador = r.randint(0,tamano-1)
        columnaGanador = r.randint(0,tamano-1)
        if not isinstance(matriz[filaGanador][columnaGanador], int):
            matriz[filaGanador][columnaGanador] = 100
            break
    while True:
        filaPerdedor = r.randint(0,tamano-1)
        columnaPerdedor = r.randint(0,tamano-1)
        if not isinstance(matriz[filaPerdedor][columnaPerdedor], int):
            matriz[filaPerdedor][columnaPerdedor] = -100
            break
    return matriz
matriz = generarTablero()
for i in matriz:
    print(i)
def main():
    pass