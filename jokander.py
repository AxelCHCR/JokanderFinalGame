import time as t
import random as r
def mostrarInfoJuego():
    print("\n¡Bienvenido a Jokander: El juego Final!")
    print(f"El juego consiste en tomar una casilla del tablero e ir encontrando puntos alrededor de él.\n\
Se tiene un número aleatorio de intentos para ganar el juego, el cual se gana con las siguientes condiciones:\n\
    - Obteniendo un 50% de los puntos positivos del tablero\n\
    - Encontrando el territorio emergente del trono Jokander.")
    print("\n¡Ten cuidado! También se puede perder el juego si:\n\
    - Se obtienen 50 puntos negativos\n\
    - Se encuentra el territorio emergente perdedor\n\
    - Se acaban los intentos")
def buscarCasilla(tablero, casilla):
    fila = int(casilla[0])
    columna = int(casilla[2:])
    print(f"La casila encontrada contiene al número {tablero[fila-1][columna-1]}")
    return (tablero[fila][columna], fila, columna)



def imprimirTablero(tablero):
    visualizacion = ""
    visualizacion += "\t\t"
    for i in range(1, len(tablero)+1):
        trozoTablero =f"{i} |\t"
        visualizacion += trozoTablero
    visualizacion += "\n"
    for i in range(1, len(tablero)+1):
        trozoTablero = f"___\n{i}\n"
        visualizacion += trozoTablero
    return visualizacion

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
"""for i in matriz:
    print(i)"""

def juego():
    mostrarInfoJuego()
    intentos = r.randint(12,18)
    casillasJugadas = []
    nombre = input("Ingrese su nombre: ")
    print(f"{nombre}, para esta partida tienes {intentos} intentos.")
    matriz = generarTablero()
    print("La casilla se solicita usando el siguiente formato:\n\
            Fila-Columna. Ejemplo: 1-2.\n")
    print(imprimirTablero(matriz))
    contadorIntentos = 0
    puntosPositivos = 0
    puntosNegativos = 0
    while contadorIntentos < intentos:
        casilla = input("Ingrese la casilla a buscar: ")
        casillaAMostrar = buscarCasilla(matriz, casilla)
        casillasJugadas.append((casillaAMostrar[1], casillaAMostrar[2]))
        if casillaAMostrar[0] == 5:
            print(f"{nombre} ha ganado 5 puntos positivos. ")
        if casillaAMostrar[0] == -5:
            print(f"{nombre} ha ganado 5 puntos negativos. ")
        if casillaAMostrar[0] == 10:
            print(f"{nombre} ha ganado 10 puntos positivos. ")
        if casillaAMostrar[0] == -10:
            print(f"{nombre} ha ganado 10 puntos negativos. ")
        if casillaAMostrar[0] == 100:
            print(f"¡{nombre} ha ganado el juego!")
        if casillaAMostrar[0] == -100:
            print(f"¡{nombre} ha ganado el juego!")
        
        print(casillasJugadas)
        contadorIntentos+=1

def main():
    juego()
main()