import random
import Menu
from LinkedList import LinkedList
from Board import Board


class Game:
    def __init__(self, board):
        self.board = board
        self.player_pos = None
        self.enemy_pos = None
        self.walls_pos = None
        self.special_ability = None


    def add_player(self):
        """
        Asignar la posición inicial del jugador 
        """
        self.player_pos = self.board.player_initial_position()


    def add_enemies(self):
        """
        Asigna la posición inicial de los enemigos
        """
        self.enemy_pos = self.board.enemies_initial_positions()

        
    def add_walls(self):
        """
        Asigna la posición inicial de los muros
        """
        self.walls_pos = self.board.walls_positions()


    def add_special_skills(self):
        """
        Asigna la posicion inicial de las cajas
        """
        self.special_pos = self.board.special_initial_positions()


    def reset_game(self):
        """
        Reinicia el juego para comenzar una nueva partida.
        """
        # Restablecer la posición del jugador
        self.board.set_cell(*self.player_pos, '🟩')

        # Reinicia el mapa
        self.board = Board(13)

        # Añade el jugador, enemigos y muros al nuevo mapa
        self.board.player_initial_position()
        self.board.enemies_initial_positions()


    def check_enemy_collision(self):
        """
        Verifica si el jugador ha chocado con un enemigo, si es así, reinicia el juego.
        """
        if self.player_pos == self.enemy_pos:
            print("¡Oh no! ¡Un enemigo te ha atrapado! ¡El juego se reiniciará.")
            self.reset_game()
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
            if node_value == '⛔':
                print("!Auch¡ parece que en esta direccion hay un muro")
                return

            # Si la direccion a la que va a saltar esta un enemigo
            if node_value == '🧟':
                print("¡Oh no! ¡Un enemigo te ha atrapado! ¡El juego se reiniciará.")
                self.lose_game()

            #Si la direccion a la que va a saltar, hay una caja de poderes especiales
            if node_value == '📦':
                self.board.set_cell(*self.player_pos, '🟩')
                self.board.set_cell(new_row, new_col, '🕺')
                print("¡Has obtenido un poder especial!")
                self.obtain_special_ability()


            else:
                self.board.set_cell(*self.player_pos, '🟩')
                self.board.set_cell(new_row, new_col, '🕺')
            self.player_pos = (new_row, new_col)
            return

        else:
            print()
            print("!Cuidado¡ te puedes caer del mapa")


    def obtain_special_ability(self):
        """
        Selecciona una habilidad especial al azar y la asigna al jugador.
        """
        if self.special_ability is not None:
            print("Ya tiene una habilidad especial")
            return

        special_abilities = ["Más bombas", "Mayor alcance de bombas"]
        self.special_ability = random.choice(special_abilities)

        if self.special_ability == "Más bombas":
            print("¡Has obtenido la habilidad de colocar más bombas en tus turnos!")
        else:
            print("¡Has obtenido la habilidad de aumentar el alcance de tus bombas a 3 casillas por lado!")


    def explode_bomb(self, row, col):
        """
        Hace explotar la bomba en la posición especificada y elimina los enemigos y paredes adyacentes.
        """

        # Define las posiciones adyacentes a la explosión segun si tiene habilidad o no
        if self.special_ability == "Mayor alcance de bombas":
            adjacent_positions = [
                (row - 1, col), (row + 1, col),  # Arriba y abajo
                (row, col - 1), (row, col + 1),  # Izquierda y derecha
                (row - 2, col), (row + 2, col),  # Dos casillas arriba y dos casillas abajo
                (row, col - 2), (row, col + 2)  # Dos casillas a la izquierda y dos casillas a la derecha
            ]
        else:
            adjacent_positions = [
                # Arriba y abajo
                (row - 1, col),
                (row + 1, col),
                # Izquierda y derecha
                (row, col - 1),
                (row, col + 1)
            ]

        for pos in adjacent_positions:
            pos_row, pos_col = pos
            if self.board.valid_position(pos_row, pos_col):
                cell_value = self.board.get_cell_value(pos_row, pos_col)
                if (cell_value == '🧟' or cell_value == '⛔'):
                    # Si hay un enemigo o una pared adyacente, los elimina
                    self.board.set_cell(pos_row, pos_col, '🟩')  # Reemplaza la celda por un espacio vacío

        self.board.set_cell(row, col, '🟩')


    def drop_bomb(self,x=0):
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
            if node_value == '⛔' or node_value == '🧟':
                self.explode_bomb(new_row, new_col)  # Hace explotar la bomba y elimina enemigos y paredes adyacentes
                print("!Boom! La bomba ha explotado")

            else:
                self.board.set_cell(new_row, new_col, '💣')# Coloca la bomba en la nueva posición
                self.explode_bomb(new_row,new_col)

        if self.special_ability == "Más bombas":

            if x == 1:
                return
            else:
                self.drop_bomb(x + 1)


    def clear_board(self):
        """
        Borra completamente el mapa estableciendo el valor de cada celda como vacío.
        """
        self.player_pos = None
        self.enemy_pos = None
        self.walls_pos = None
        self.special_ability = None

        for row in range(13):
            for col in range(13):
                self.board.set_cell(row, col, '🟩')


    def lose_game(self):
        self.clear_board()
        Menu.menu_bomberman()
        return
