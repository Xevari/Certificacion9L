# Juego del Gato / Tic Tac Toe

import random

#Impresión de tablero

def TableroDeDibujo(tablero):

    print(tablero[7] + '|' + tablero[8] + '|' + tablero[9])
    print('-+-+-')
    print(tablero[4] + '|' + tablero[5] + '|' + tablero[6])
    print('-+-+-')
    print(tablero[1] + '|' + tablero[2] + '|' + tablero[3])

def letraIntroducidaPorJugador():
    #Se va a dejar escojer al jugador que letra quiere ser X o O.
    #Regresa una lista con la del primer jugador como la primera cosa, y la letra de la computadora como la segunda cosa.
    letra = ''
    while not (letra == 'X' or letra == 'O'):
        print('¿Quieres ser X o O?')
        letra = input().upper()
        
#El primer elemento del juego es la letra del jugador, el segundo elemento del juego es de la computadora.

    if letra == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def quienVaPrimero():
    #Aleatoriamente va a escojer que jugador va primero
    if random.randint (0, 1) == 0:
        return 'Computadora'
    else:
        return 'Jugador'
    
def HacerMovimiento(tablero, letra, movimiento):
    tablero[movimiento] = letra

def esGanador(tab, let):
    #Esta función regresa true si el jugador a Ganado.
    #Se abrevió tablero por tab y letra por let, para no escribir tanto.

    return ((tab[7] == let and tab[8] == let and tab[9] == let) or # alrededor de la parte superior
            (tab[4] == let and tab[5] == let and tab[6] == let) or # alrededor de la parte media
            (tab[1] == let and tab[2] == let and tab[3] == let) or # alrededor de la parte inferior
            (tab[7] == let and tab[4] == let and tab[1] == let) or # abajo en el lado izquiero del tablero
            (tab[8] == let and tab[5] == let and tab[2] == let) or # abajo en medio del tablero
            (tab[9] == let and tab[6] == let and tab[3] == let) or # abajo en el lado derecho del tablero
            (tab[7] == let and tab[5] == let and tab[3] == let) or # diagonal en el tablero
            (tab[9] == let and tab[5] == let and tab[1] == let)) # diagonal en el tablero

#Hace una copia de la lista del tablero y la regresa.
def obtenerCopiaDeTablero(tablero):
    copiaTablero = []
    for i in tablero:
        copiaTablero.append(i)
    return copiaTablero

def esEspacioLibre(tablero,movimiento):
    #Regresa true si el movimiento es libre en el tablero.
    return tablero[movimiento] == ' '

def obtenerMovimientoDelJugador(tablero):
    #Deja que el jugador escriba su movimiento.
    movimiento = ' '
    while movimiento not in '1 2 3 4 5 6 7 8 9'.split() or not esEspacioLibre(tablero,int(movimiento)):
        print('Cual es el siguiente movimiento? (1-9)')
        movimiento = input()
    return int(movimiento)

def elegirMovimientoAleatorioDesdeLista(tablero, listaDeMovimientos):
    #Devuelve un movimiento válido desde la lista pasada en el tablero pasado
    #Devuelve none si no hay movimiento válido.
    movimientosPosibles = []
    for i in listaDeMovimientos:
        if esEspacioLibre(tablero, i):
            movimientosPosibles.append(i)

    if len(movimientosPosibles) != 0:
        return random.choice(movimientosPosibles)
    else:
        return None
    
def obtenerMovimientoDeComputadora(tablero, letraComputadora):
    #Dado un tablero y la letra de la computadora determina donde mover y regresar ese valor.
    if letraComputadora == 'X':
        letraJugador ='O'
    else:
        letraJugador ='X'

    #Aquí está nuestro algoritmo para nuestra inteligencia artificial de nuestro juego del gato
    #Primero, checa si podemos ganar nuestro siguiente movimiento.

    for i in range(1, 10):
        copiaTablero = obtenerCopiaDeTablero(tablero)
        if esEspacioLibre(copiaTablero, i):
            HacerMovimiento(copiaTablero, letraComputadora, i)
            if esGanador (copiaTablero, letraComputadora):
                return i
    
    #Valida si el jugador podria ganar en su siguiente movimiento y los bloquea.
    for i in range(1, 10):
        copiaTablero = obtenerCopiaDeTablero(tablero)
        if esEspacioLibre(copiaTablero, i):
            HacerMovimiento(copiaTablero, letraJugador, i)
            if esGanador(copiaTablero, letraJugador):
                return i
    
    #Trata de tomar un lugar en la esquina si estan libres.

    movimiento = elegirMovimientoAleatorioDesdeLista(tablero, [1, 3, 7, 9])
    if movimiento != None:
        return movimiento
    
    #Trata de tomar el centro si está libre.
    if esEspacioLibre(tablero, 5):
        return 5
    
    #Moverse sobre alguno de los lados
    return elegirMovimientoAleatorioDesdeLista(tablero, [2, 4, 6, 8])

def estaElTableroLleno(tablero):
    #Devuelve True si cada espacio del tablero a sido tomado. De otra manera, devuelve False.
    for i in range(1, 10):
        if esEspacioLibre(tablero, i):
            return False
        return True
    
print('Bienvenido al juego del Gato!')
while True:
    #Resetear el tablero
    elTablero = [' '] * 10
    letraJugador, letraComputadora = letraIntroducidaPorJugador()
    turno = quienVaPrimero()
    print(turno + 'ira primero.')
    elJuegoSeEstaJugando = True

    while elJuegoSeEstaJugando:
        if turno == 'Jugador':
            #Turno del Jugador.
            TableroDeDibujo(elTablero)
            movimiento = obtenerMovimientoDelJugador(elTablero)
            HacerMovimiento (elTablero, letraJugador, movimiento)

            if esGanador(elTablero, letraJugador):
                TableroDeDibujo(elTablero)
                print('Has Ganado el Juego!')
                elJuegoSeEstaJugando = False
            else:
                if estaElTableroLleno(elTablero):
                   TableroDeDibujo(elTablero)
                   print('El juego terminó en Empate!')
                   break
                else:
                    turno = 'Computadora'
        else:
            #Turno de la Computadora
            movimiento = obtenerMovimientoDeComputadora(elTablero, letraComputadora)
            HacerMovimiento(elTablero, letraComputadora, movimiento)

            if esGanador(elTablero, letraComputadora):
                TableroDeDibujo(elTablero)
                print('La Computadora ha ganado! Game Over!')
                elJuegoSeEstaJugando = False
            else:
                if estaElTableroLleno(elTablero):
                   TableroDeDibujo(elTablero)
                   print('El juego terminó en Empate!')
                   break
                else:
                        turno = 'Jugador'
    
    print('Quieres jugar de nuevo? (Sí o No)')
    if not input().lower().startswith('si'):
        break



