from LinkedList import LinkedList
import random

class Board:
    
    def __init__(self, n: int):
        self.n: int = n
        self.board = self.create_board()


    def get_board_size(self):
        """
        Devuelve el tamaño del tablero
        """
        return self.n


    def create_board(self, board = None, current_row: int = 0):
        """
        Crea el tablero recursivamente utilizando la lista enlazada
        """
        if board is None: # Si el tablero no existe, se crea una nueva instancia de la clase LinkedList()
            board = LinkedList()
            
        if current_row == self.n: # Si ya se alzanco el numero de filas retorna el tablero creado
            return board
        
        row = LinkedList()
        
        for columns in range(self.n): # Crea "self.n" columnas en la fila
            row.add_head(None)
            
        board.add_head(row)
        
        return  self.create_board(board, current_row + 1)
    
    
    def print_board(self):
        """
        Imprime el tablero en la consola
        """
        curr_row = self.board.head
        
        while curr_row: # Itera a traves de cada fila
            curr_node = curr_row.value.head
            row_str = ''
            
            while curr_node: # Itera a traves de los nodos de cada fila
                row_str += curr_node.value
                curr_node = curr_node.next
                
            print(row_str)
            curr_row = curr_row.next
    

    def add_symbol(self):
        """
        Agrega el simbolo 🟩 como inical en el tablero
        """
        symbol_table = '🟩'
        curr_row = self.board.head

        while curr_row: # Itera a traves de las filas del tablero
            curr_node = curr_row.value.head

            while curr_node: # Itera a traves de los nodos de cada fila
                if curr_node.value is None: # Si el valor del nodo es None se añade el "symbol_table"
                    curr_node.value = symbol_table

                curr_node = curr_node.next

            curr_row = curr_row.next
            
            
    def valid_position(self, row, col) -> bool:
        """
        Verifica si una posicion dada esta dentro de los limites del tablero
        """
        return 0 <= row < self.n and 0 <= col < self.n
    
    
    def set_cell(self, row, col, value):
        """
        Establece el valor de la celda en la posicion dada
        """
        curr_row = self.board.head

        for row in range(row): # Avanzar hasta la fila especificada
            curr_row = curr_row.next

        curr_node = curr_row.value.head
        
        for col in range(col): # Avanzar hasta la columna especificada
            curr_node = curr_node.next

        curr_node.value = value # Establece el valor del nodo actual por el valor requerido


    def get_cell_value(self, row, col):
        """
        Obtiene el valor de la celda en la posicion dada
        """
        curr_row = self.board.head

        for row in range(row):
            curr_row = curr_row.next # Pasar a la siguiente fila

        curr_node = curr_row.value.head
        
        for col in range(col): # Avanzar hasta la columna especificada
            curr_node = curr_node.next

        return curr_node.value
    
    
    def player_initial_position(self):
        """
        Establece la posicion inicial del jugador
        """
        row = 0
        col = 0
        player_symbol = '🕺'

        self.set_cell(row, col, player_symbol)
        return row, col


    def special_initial_positions(self, num_special = 2, x=0):
        """
        Agrega dos habilidades especiales aleatorias al tablero.
        """
        special_symbol = '📦'

        if x == num_special:
            return
        else:
            while True:
                row = random.randint(0, self.n - 1)
                col = random.randint(0, self.n - 1)
                cell_value = self.get_cell_value(row, col)
                if cell_value is None or cell_value == '🟩' or cell_value == '🧟' or cell_value == '⛔':
                    self.set_cell(row, col, special_symbol)
                    break
            self.special_initial_positions(num_special, x + 1)

    def enemies_initial_positions(self, num_enemies = random.randint(8, 13), x = 0):
        """
        Estable las posiciones inciales de los enemigos en el tablero de forma aleatoria
        """
        enemy_symbol = '🧟'
        
        if x == num_enemies:
            return
        else:
            row = random.randint(0, self.n - 1)
            col = random.randint(1, self.n - 1)
            if self.get_cell_value(row, col) != '🕺' and '🧟' and '📦' :  # Verificar si la casilla no contiene el jugador
                self.set_cell(row, col, enemy_symbol)
            self.enemies_initial_positions(num_enemies, x + 1)
                
                
    def walls_positions(self, num_walls=80, x=0):
        """
        Establece la posiciones de los muros de la tablero
        """
        wall_symbol = '⛔'
        
        if x == num_walls:
            return
        else:
            row = random.randint(0, self.n - 1)
            col = random.randint(0, self.n - 1)
            if self.get_cell_value(row, col) != '🕺' and '🧟' and '📦':  # Verificar si la casilla no contiene el jugador o los enemigos
                self.set_cell(row, col, wall_symbol)
            self.walls_positions(num_walls, x + 1)

    def is_empty(self, row, col):
        """
        Verifica si la celda especificada por fila y columna está vacía.
        """
        cell_value = self.board.get_cell_value(row, col)
        return cell_value is None or cell_value == '🟩'

    def find_enemies(self):
        """
        Busca enemigos en el tablero, retorna False si encuentra al menos un enemigo, True si no encuentra ninguno.
        """
        curr_row = self.board.head

        while curr_row:  # Itera a través de las filas del tablero
            curr_node = curr_row.value.head

            while curr_node:  # Itera a través de los nodos de cada fila
                if curr_node.value == '🧟':  # Si encuentra un enemigo, retorna False
                    return False
                curr_node = curr_node.next

            curr_row = curr_row.next

        return True