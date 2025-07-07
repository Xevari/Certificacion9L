import random
import copy

class AgenteTicTacToe:
    def __init__(self, jugador):
        self.jugador = jugador  # 'X' u 'O'
        self.tablero = None
        self.jugador_actual = None
    
    def percibir(self, estado_tablero, jugador_actual):
        self.tablero = estado_tablero
        self.jugador_actual = jugador_actual
    
    def _evaluar_estado(self, tablero):
        """
        Evalúa el estado actual del tablero y devuelve:
        - 10 si el agente gana
        - -10 si el oponente gana
        - 0 si es empate
        - None si el juego continúa
        """
        oponente = 'X' if self.jugador == 'O' else 'O'
        
        # Verificar si el agente gana
        if verificar_ganador(tablero, self.jugador):
            return 10
        # Verificar si el oponente gana
        elif verificar_ganador(tablero, oponente):
            return -10
        # Verificar empate
        elif all(tablero[i][j] != " " for i in range(3) for j in range(3)):
            return 0
        # El juego continúa
        else:
            return None
    
    def minimax(self, tablero, es_maximizando):
        """
        Implementación del algoritmo Minimax (recursivo)
        - tablero: estado actual del tablero
        - es_maximizando: True si es el turno del agente (MAX), False si es turno del oponente (MIN)
        Devuelve: (valor, mejor_movimiento)
        """
        # Evaluar el estado actual
        valor_estado = self._evaluar_estado(tablero)
        if valor_estado is not None:
            return (valor_estado, None)
        
        # Inicializar mejor valor y mejor movimiento
        if es_maximizando:
            mejor_valor = -float('inf')
            jugador_actual = self.jugador  # Agente (MAX)
        else:
            mejor_valor = float('inf')
            jugador_actual = 'X' if self.jugador == 'O' else 'O'  # Oponente (MIN)
        
        mejor_movimiento = None
        movimientos_optimos = []  # Para almacenar múltiples movimientos óptimos
        
        # Explorar todos los movimientos posibles
        for i in range(3):
            for j in range(3):
                if tablero[i][j] == " ":
                    # Hacer una copia profunda para no modificar el tablero original
                    nuevo_tablero = copy.deepcopy(tablero)
                    nuevo_tablero[i][j] = jugador_actual
                    
                    # Llamada recursiva a minimax
                    valor, _ = self.minimax(nuevo_tablero, not es_maximizando)
                    
                    # Evaluar para jugador MAX (agente)
                    if es_maximizando:
                        if valor > mejor_valor:
                            mejor_valor = valor
                            mejor_movimiento = (i, j)
                            movimientos_optimos = [(i, j)]  # Reiniciar lista de óptimos
                        elif valor == mejor_valor:
                            movimientos_optimos.append((i, j))
                    
                    # Evaluar para jugador MIN (oponente)
                    else:
                        if valor < mejor_valor:
                            mejor_valor = valor
                            mejor_movimiento = (i, j)
                            movimientos_optimos = [(i, j)]  # Reiniciar lista de óptimos
                        elif valor == mejor_valor:
                            movimientos_optimos.append((i, j))
        
        # Si hay múltiples movimientos óptimos, elegir uno aleatoriamente
        if movimientos_optimos:
            mejor_movimiento = random.choice(movimientos_optimos)
        
        return (mejor_valor, mejor_movimiento)
    
    def tomar_accion(self):
        """
        Determina la acción óptima usando el algoritmo Minimax
        """
        if self.jugador_actual != self.jugador:
            return None
        
        # Obtener celdas vacías
        celdas_vacias = []
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == " ":
                    celdas_vacias.append((i, j))
        
        if not celdas_vacias:
            return None
        
        # Si es el primer movimiento, elegir aleatoriamente para optimizar rendimiento
        # (todos los primeros movimientos son simétricamente equivalentes)
        if len(celdas_vacias) == 9:
            return random.choice([(0, 0), (0, 2), (2, 0), (2, 2), (1, 1)])
        
        # Usar Minimax para determinar el mejor movimiento
        _, mejor_movimiento = self.minimax(self.tablero, True)
        return mejor_movimiento

def imprimir_tablero(tablero):
    """
    Imprime el tablero de juego en la consola
    """
    print("\n  0 | 1 | 2")
    for i, fila in enumerate(tablero):
        print(f"{i} {' | '.join(fila)}")
        if i < 2:
            print(" ---|---|---")

def verificar_ganador(tablero, jugador):
    """
    Verifica si un jugador ha ganado
    """
    # Verificar filas y columnas
    for i in range(3):
        if all(tablero[i][j] == jugador for j in range(3)):  # Filas
            return True
        if all(tablero[j][i] == jugador for j in range(3)):  # Columnas
            return True
    
    # Verificar diagonales
    if all(tablero[i][i] == jugador for i in range(3)):  # Diagonal principal
        return True
    if all(tablero[i][2-i] == jugador for i in range(3)):  # Diagonal secundaria
        return True
    
    return False

def elegir_jugador():
    """
    Permite al usuario elegir su símbolo (X u O)
    """
    while True:
        eleccion = input("\n¿Quieres jugar como X o como O? (X/O): ").upper()
        if eleccion in ['X', 'O']:
            return eleccion
        else:
            print("Opción inválida. Por favor elige 'X' u 'O'.")

def jugar_tres_en_raya():
    """
    Función principal para ejecutar el juego
    """
    print("¡Bienvenidos al 3 en raya con IA inteligente!")
    print("-------------------------------------------\n")
    
    # Permitir al usuario elegir su símbolo
    jugador_humano = elegir_jugador()
    jugador_agente = 'O' if jugador_humano == 'X' else 'X'
    
    # Crear agente
    agente = AgenteTicTacToe(jugador_agente)
    
    # Mensaje informativo
    print(f"\nJugador Humano: {jugador_humano}")
    print(f"Jugador Agente: {jugador_agente}")
    print("\nNota: El agente puede tardar unos segundos en movimientos complejos.")
    print("      ¡Por favor sea paciente!\n")
    
    # Bucle principal para múltiples partidas
    while True:
        # Inicializar tablero y variables de juego
        tablero = [[" " for _ in range(3)] for _ in range(3)]
        jugadores = ['X', 'O']
        turno = 0  # Empieza X
        
        # Bucle para una sola partida
        for _ in range(9):
            jugador_actual = jugadores[turno % 2]
            imprimir_tablero(tablero)
            
            if jugador_actual == jugador_humano:  # Turno humano
                while True:
                    try:
                        fila = int(input(f"\nJugador {jugador_humano} - Fila (0-2): "))
                        col = int(input(f"Jugador {jugador_humano} - Columna (0-2): "))
                        if 0 <= fila <= 2 and 0 <= col <= 2:
                            if tablero[fila][col] == " ":
                                tablero[fila][col] = jugador_humano
                                break
                            else:
                                print("¡Casilla ocupada! Intenta de nuevo.")
                        else:
                            print("¡Coordenadas inválidas! Usa valores entre 0-2.")
                    except ValueError:
                        print("¡Entrada inválida! Ingresa números enteros.")
            else:  # Turno del agente
                print(f"\nPensando el agente ({jugador_agente})...")
                agente.percibir(tablero, jugador_actual)
                movimiento = agente.tomar_accion()
                if movimiento is None:
                    print("\n¡Error! El agente no encontró movimiento válido.")
                    break
                fila, col = movimiento
                tablero[fila][col] = jugador_agente
                print(f"Agente ({jugador_agente}) juega: Fila {fila}, Columna {col}")
            
            # Verificar si hay ganador
            if verificar_ganador(tablero, jugador_actual):
                imprimir_tablero(tablero)
                if jugador_actual == jugador_humano:
                    print(f"\n¡Felicidades! Has ganado contra la IA.")
                else:
                    print(f"\n¡El agente ({jugador_agente}) ha ganado!")
                break
            
            turno += 1
        else:
            # Si no hay ganador después de 9 movimientos, es empate
            imprimir_tablero(tablero)
            print("\n¡Empate! Nadie ha ganado.")
        
        # Preguntar si desea jugar otra partida
        while True:
            continuar = input("\n¿Deseas jugar otra partida? (sí/no): ").lower()
            if continuar in ['sí', 'si', 's', 'yes', 'y']:
                print("\n" + "="*50)
                print("¡Nueva partida!".center(50))
                print("="*50 + "\n")
                break
            elif continuar in ['no', 'n']:
                print("\n¡Gracias por jugar! Hasta la próxima.")
                return
            else:
                print("Respuesta inválida. Por favor responde 'sí' o 'no'.")

if __name__ == "__main__":
    jugar_tres_en_raya()