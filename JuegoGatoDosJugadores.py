def imprimir_tablero(tablero):
    print("\n  0 | 1 | 2")
    for i, fila in enumerate(tablero):
        print(f"{i} {' | '.join(fila)}")
        if i < 2:
            print(" ---|---|---")

def verificar_ganador(tablero, jugador):
    # Verificar filas y columnas
    for i in range(3):
        if all(tablero[i][j] == jugador for j in range(3)):  # Filas
            return True
        if all(tablero[j][i] == jugador for j in range(3)):  # Columnas
            return True
            
    # Verificar diagonales
    if all(tablero[i][i] == jugador for i in range(3)) or \
       all(tablero[i][2-i] == jugador for i in range(3)):
        return True
        
    return False

def jugar_tres_en_raya():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugadores = ["X", "O"]
    turno = 0
    
    print("¡Bienvenidos al 3 en raya!")
    print("Jugador 1: X\nJugador 2: O")
    
    for _ in range(9):
        jugador_actual = jugadores[turno % 2]
        imprimir_tablero(tablero)
        
        while True:
            try:
                fila = int(input(f"\nJugador {jugador_actual} - Fila (0-2): "))
                col = int(input(f"Jugador {jugador_actual} - Columna (0-2): "))
                
                if 0 <= fila <= 2 and 0 <= col <= 2:
                    if tablero[fila][col] == " ":
                        tablero[fila][col] = jugador_actual
                        break
                    else:
                        print("¡Casilla ocupada! Intenta de nuevo.")
                else:
                    print("¡Coordenadas inválidas! Usa valores entre 0-2.")
            except ValueError:
                print("¡Entrada inválida! Ingresa números enteros.")
        
        if verificar_ganador(tablero, jugador_actual):
            imprimir_tablero(tablero)
            print(f"\n¡Felicidades! Jugador {jugador_actual} ha ganado.")
            return
            
        turno += 1
    
    imprimir_tablero(tablero)
    print("\n¡Empate! Nadie ha ganado.")

if __name__ == "__main__":
    jugar_tres_en_raya()