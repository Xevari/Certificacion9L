import random

class AgenteTicTacToe:
    def __init__(self, jugador):
        self.jugador = jugador  # 'X' u 'O'
        self.tablero = None
        self.jugador_actual = None
    
    def percibir(self, estado_tablero, jugador_actual):
        self.tablero = estado_tablero
        self.jugador_actual = jugador_actual
    
    def tomar_accion(self):
        if self.jugador_actual != self.jugador:
            return None
        
        celdas_vacias = []
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == " ":
                    celdas_vacias.append((i, j))
        
        if not celdas_vacias:
            return None
        
        return random.choice(celdas_vacias)

def imprimir_tablero(tablero):
    print("\n  0 | 1 | 2")
    for i, fila in enumerate(tablero):
        print(f"{i} {' | '.join(fila)}")
        if i < 2:
            print(" ---|---|---")

def verificar_ganador(tablero, jugador):
    for i in range(3):
        if all(tablero[i][j] == jugador for j in range(3)):
            return True
        if all(tablero[j][i] == jugador for j in range(3)):
            return True
    if all(tablero[i][i] == jugador for i in range(3)) or \
       all(tablero[i][2-i] == jugador for i in range(3)):
        return True
    return False

def jugar_tres_en_raya():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugadores = ["X", "O"]
    turno = 0
    agente = AgenteTicTacToe('O')  # Agente juega con 'O'

    print("¡Bienvenidos al 3 en raya!")
    print("Jugador 1 (Humano): X")
    print("Jugador 2 (Agente): O\n")
    
    for _ in range(9):
        jugador_actual = jugadores[turno % 2]
        imprimir_tablero(tablero)
        
        if jugador_actual == 'X':  # Turno humano
            while True:
                try:
                    fila = int(input(f"\nJugador X - Fila (0-2): "))
                    col = int(input(f"Jugador X - Columna (0-2): "))
                    if 0 <= fila <= 2 and 0 <= col <= 2:
                        if tablero[fila][col] == " ":
                            tablero[fila][col] = 'X'
                            break
                        else:
                            print("¡Casilla ocupada! Intenta de nuevo.")
                    else:
                        print("¡Coordenadas inválidas! Usa valores entre 0-2.")
                except ValueError:
                    print("¡Entrada inválida! Ingresa números enteros.")
        else:  # Turno del agente
            agente.percibir(tablero, jugador_actual)
            movimiento = agente.tomar_accion()
            if movimiento is None:
                print("\n¡Error! El agente no encontró movimiento válido.")
                break
            fila, col = movimiento
            tablero[fila][col] = 'O'
            print(f"\nAgente (O) juega: Fila {fila}, Columna {col}")
        
        if verificar_ganador(tablero, jugador_actual):
            imprimir_tablero(tablero)
            print(f"\n¡Felicidades! Jugador {jugador_actual} ha ganado.")
            return
        turno += 1
    
    imprimir_tablero(tablero)
    print("\n¡Empate! Nadie ha ganado.")

if __name__ == "__main__":
    jugar_tres_en_raya()