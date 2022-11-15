#Tecnológico de Costa Rica
#Elementos de Computación - Proyecto Final
#Autores: Javier Vásquez, Axel Chaves
import datetime as dt
import random as r

def validarIngresoCasilla(casilla, largo): #Valida que la casilla ingresada sea válida. 
    separacion = casilla.split("-")
    formatoInvalido = "La casilla no cumple con el formato. "
    if len(separacion) != 2: #Si se separó correctamente
        print(formatoInvalido)
        return False
    if not isinstance(eval(separacion[0]), int) or not isinstance(eval(separacion[1]), int): #Si son enteros
        print(formatoInvalido)
        return False
    if eval(separacion[0]) not in range(1,largo+1) or eval(separacion[1]) not in range(1,largo+1): #Si está fuera del rango del tablero
        print("La casilla ingresada no existe. ")
        return False
    return True
def continuarJuego(): #Se le pregunta al usuario si desea continuar y continúa. Sino, cierra el programa. 
    while True:
        decision = input("¿Desea continuar? (y/n): ")
        if decision.lower() == "y":
            juego()
        elif decision.lower() == "n":
            print("Juego terminado. ")
            exit()
def guardarPartida(jugador, puntosTotales, estado, emergente): #Guarda los datos de la partida. 
    fechaHora = dt.datetime.now() #Fecha y hora del sistema.
    archivo = open("Juegos.dat", "a")
    archivo.write(f"Fecha: {fechaHora}, Jugador: {jugador}, PuntosTotales: {puntosTotales}, Estado: {estado}, Terrtorio emergente: {emergente}.")
    archivo.close()
def llenarCasillas(tope,tamano, matriz, valor): #Llena el tablero con los puntos en posiciones aleatorias. 
    contador = 0
    while True:
        if contador == tope:
            break
        fila = r.randint(0,tamano-1)
        columna = r.randint(0, tamano-1)
        if not isinstance(matriz[fila][columna], int):
            matriz[fila][columna] = valor
            contador += 1
def llenarTerritorios(tamano, matriz, valor):
    while True:
        filaGanador = r.randint(0,tamano-1)
        columnaGanador = r.randint(0,tamano-1)
        if not isinstance(matriz[filaGanador][columnaGanador], int):
            matriz[filaGanador][columnaGanador] = valor
            break 
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
    casillas = casilla.split("-")
    fila = int(casillas[0])-1
    columna = int(casillas[1])-1
    print(f"La casila encontrada contiene al número {tablero[fila][columna]}")
    return (tablero[fila][columna], (fila+1, columna+1)) #Regresa la casilla encontrada y una tupla con la posición jugada por el usuario.
def imprimirTablero(tablero, fichasJugadas = []): #Imprime el tablero con las posiciones jugadas. 
    visualizacion = ""
    visualizacion += "\t" #Estética
    for i in range(1, len(tablero)+1): #Recorre el tablero para darle formato a la impresión.
        trozoTablero =f"{i} |\t\t"
        visualizacion += trozoTablero
    visualizacion += "\n"
    listaAImprimir = []
    for i in range(0, len(tablero)): #Crea la lista que imprime lo que se ha jugado en el tablero.
        listaAImprimir.append([])
    for i in listaAImprimir:
        for j in range(0, len(tablero)): #Rellena la lista a imprimir.
            listaAImprimir[j].append("-")
    if isinstance(fichasJugadas, list) and len(fichasJugadas) != 0:
        contador = 0
        while contador < len(fichasJugadas): #Reemplaza los "-" por el puntaje en las posiciones ya jugadas.
            fila = (fichasJugadas[contador][0])-1
            columna = (fichasJugadas[contador][1])-1
            listaAImprimir[fila][columna] = tablero[fila][columna]
            contador += 1
    for i in range(1, len(tablero)+1): #Recorre el tablero, agregando los indicadores de columnas y las posiciones jugadas y no jugadas.
        posicion = ""
        trozoTablero = f"\n___\n{i}" 
        visualizacion += trozoTablero
        for elemento in listaAImprimir[i-1]:
            posicion += f"  \t{elemento}\t"
        visualizacion += posicion
    return visualizacion #Retorna la tabla a visualizar
def generarTablero():
    tamano = r.randint(8,10) #Genera el tamaño aleatorio del tablero
    matriz = []
    for i in range(0, tamano):
        matriz.append([[]*tamano]*tamano) #Genera el tablero vacío
    #Las siguientes son variables que determinan cuántas posiciones del tablero se determinarán a cada puntaje
    totalCasillas = pow(tamano,2)
    ganarCincoPuntos = int(totalCasillas*0.3)
    ganarDiezPuntos = int(totalCasillas*0.15)
    perderCincoPuntos = int(totalCasillas*0.3)
    perderDiezPuntos = int(totalCasillas*0.15)
    restantes = totalCasillas-ganarCincoPuntos-ganarDiezPuntos-perderCincoPuntos-perderDiezPuntos
    #Aquí, se llenan las casillas.
    llenarCasillas(ganarCincoPuntos, tamano, matriz, 5)
    llenarCasillas(ganarDiezPuntos, tamano, matriz, 10)
    llenarCasillas(perderCincoPuntos, tamano, matriz, -5)
    llenarCasillas(perderDiezPuntos, tamano, matriz, -10)
    llenarCasillas(restantes-2, tamano, matriz, 0)
    llenarTerritorios(tamano, matriz,100)
    llenarTerritorios(tamano, matriz,-100)    
    return matriz #Se retorna el tablero lleno.
contadorTiradas = 0 #Cuenta las veces que se ha jugado una partida.
def juego():
    global contadorTiradas
    casillasJugadas = []
    intentos = r.randint(12,18) #Genera la cantidad de intentos.
    if contadorTiradas == 0: #Si es la primera vez que se juega, se muestran las instrucciones. 
        mostrarInfoJuego()
    contadorTiradas += 1
    nombre = input("Ingrese su nombre: ")
    print(f"{nombre}, para esta partida tienes {intentos} intentos.")
    matriz = generarTablero()
    print("La casilla se solicita usando el siguiente formato:\n\
            Fila-Columna. Ejemplo: 1-2.\n")
    print(imprimirTablero(matriz, True))
    contadorIntentos = 0
    puntosPositivos = 0
    puntosNegativos = 0
    while True:
        #Condicionales que indican si se ganó o se perdió.
        if contadorIntentos == intentos:
            print("¡Perdiste! Se han acabado los intentos. ")
            guardarPartida(nombre, puntosPositivos+puntosNegativos, "Derrota", "No")
            continuarJuego()
        elif (len(matriz) == 8 and puntosPositivos >= 92) or (len(matriz) == 9 and puntosPositivos >= 120) or \
            len(matriz) == 10 and puntosPositivos >= 150:
            print("¡Has ganado muchos puntos, victoria!")
            print(f"PuntosTotales: {puntosPositivos+puntosNegativos}")
            guardarPartida(nombre, puntosPositivos+puntosNegativos, "Victoria", "Sí")
            continuarJuego()    
        elif puntosNegativos >= 50:
            print("¡Has perdido! Has acumulado muchos puntos negativos.")
            guardarPartida(nombre, puntosPositivos+puntosNegativos, "Derrota", "Sí")
            continuarJuego()
        while True: #Valida que se ingrese correctamente la casilla. 
            casilla = input("Ingrese la casilla a buscar: ")
            if validarIngresoCasilla(casilla, len(matriz)):
                break
            else: 
                continue
        casillaAMostrar = buscarCasilla(matriz, casilla)
        if casillaAMostrar[1] in casillasJugadas:
            print("Esta casilla ya fue jugada. ")
        elif casillaAMostrar[0] == 5:
            print(f"{nombre} ha ganado 5 puntos positivos. ")
            puntosPositivos += 5
        elif casillaAMostrar[0] == -5:
            print(f"{nombre} ha ganado 5 puntos negativos. ")
            puntosNegativos += 5
        elif casillaAMostrar[0] == 10:
            print(f"{nombre} ha ganado 10 puntos positivos. ")
            puntosPositivos += 10
        elif casillaAMostrar[0] == -10:
            print(f"{nombre} ha ganado 10 puntos negativos. ")
            puntosNegativos += 10
        elif casillaAMostrar[0] == 100:
            print(f"¡Encontraste el territorio emergente, victoria!")
            guardarPartida(nombre, puntosPositivos+puntosNegativos, "Victoria", "Sí")
            continuarJuego()
        elif casillaAMostrar[0] == -100:
            print(f"¡Encontraste el territorio emergente, derrota!")
            guardarPartida(nombre, puntosPositivos+puntosNegativos, "Derrota", "Sí")
            continuarJuego()
        else:
            print(f"{nombre} no gana puntos esta ronda. ")
        #Se indican las estadísticas de la partida. 
        print(f"Cantidad de puntos ganados: {puntosPositivos}\nCantidad de puntos perdidos: {puntosNegativos}\
                \nIntentos usados: {contadorIntentos}\nIntentos restantes: {intentos-contadorIntentos}")
        #Se agrega la casilla jugada, se cuenta un intento más y se imprime la condición actual del tablero
        casillasJugadas.append(casillaAMostrar[1])
        contadorIntentos+=1
        print(imprimirTablero(matriz, casillasJugadas))
def main():
    juego()
main()
