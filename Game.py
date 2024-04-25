import random
from LinkedList import LinkedList
import Board

class Game:
    def __init__(self, board):
        self.board = board
        self.player_pos = None
        self.enemy_pos = None
        self.walls_pos = None


    def add_player(self):
        """
        Asignar la posición inicial del jugador 
        """
        self.player_pos = self.board.player_initial_position()


    def add_enemies(self):
        """
        Asigna la posición inicial de los enemigos
        """
        self.black_pos = self.board.enemies_initial_positions()
        
        
    def add_walls(self):
        """
        Asigna la posición inicial de los muros
        """
        self.walls_pos = self.board.walls_positions()

    def reset_game(self):
        """
        Reinicia el juego para comenzar una nueva partida.
        """
        # Restablecer la posición del jugador
        self.board.set_cell(*self.player_pos, '🟩')

        self.player_pos = self.board.player_initial_position()

        # Restablecer la posición de los enemigos
        self.enemy_pos = self.board.enemies_initial_positions()

    def check_enemy_collision(self):
        """
        Verifica si el jugador está en la misma posición que un enemigo, si es así, el jugador pierde.
        """
        if self.player_pos == self.enemy_pos:
            return True
        return False


    def move_player(self, direction):
        """
        Permite hacer los movimientos del jugador blanco a eleccion del usuario
        """
        new_row, new_col = self.player_pos
        print()
        if direction == 1:  # Arriba
            new_row -= 1
        elif direction == 2:  # Abajo
            new_row += 1
        elif direction == 3:  # Izquierda
            new_col -= 1
        elif direction == 4:  # Derecha
            new_col += 1
        else:
            print('Direccion invalida, intenta de nuevo')
            self.move_player()

        if self.board.valid_position(new_row, new_col): # Verifica si la nueva posición (new_row, new_col) está dentro de los límites del tablero
            node_value = self.board.get_cell_value(new_row, new_col)

            # Si la celda a la que va a saltar es una celda con pared
            if node_value == '⬜':
                print("!Auch¡ parece que en esta direccion hay un muro")
                return

            # Si la direccion a la que va a saltar esta un enemigo
            if node_value == '👽':
                print("¡Oh no! ¡Un enemigo te ha atrapado! ¡El juego se reiniciará.")
                self.reset_game()

            else:
                self.board.set_cell(*self.player_pos, '🟩')
                self.board.set_cell(new_row, new_col, '🤖')
            self.player_pos = (new_row, new_col)
            return

        else:
            print()
            print("!Cuidado¡ te puedes caer del mapa")


    def drop_bomb(self):
        """
        Permitira ubicar las bombas, y hacer las explosion de estas
        """
        direction = int(input(
            """
            Directions
            1. Arriba
            2. Abajo
            3. Izquierda
            4. Derecha
            opcion: """))

        new_row, new_col = self.player_pos
        print()
        print()
        if direction == 1:  # Arriba
            new_row -= 1
        elif direction == 2:  # Abajo
            new_row += 1
        elif direction == 3:  # Izquierda
            new_col -= 1
        elif direction == 4:  # Derecha
            new_col += 1
        else:
            print('Invalid direction, try again')
            self.drop_bomb()

        if self.board.valid_position(new_row, new_col):  # Verifica si la nueva posición (new_row, new_col) está dentro de los límites del tablero
            node_value = self.board.get_cell_value(new_row, new_col)

            # Si la celda a la que va a saltar es una celda con pared
            if node_value == '⬜' or node_value == '👽':
                self.board.explode_bomb(new_row, new_col)  # Hace explotar la bomba y elimina enemigos y paredes adyacentes
                print("!Boom! La bomba ha explotado")
                return

            else:
                self.board.set_cell(new_row, new_col, '💣')# Coloca la bomba en la nueva posición
                self.board.explode_bomb(new_row,new_col)

            return
