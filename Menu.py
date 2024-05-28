import sys
from Board import Board
from Game import Game

board = Board(13)
game = Game(board)

def menu_bomberman():
    """
    Menu del juego, esta tanto el menu inicial, como el menu de juego
    """
    while True:
        option = int(input("""
---------- Menu Bomberman ----------
         
            1. Iniciar Bomberman
             2. Salir
               option: """))
        
        print("-----------------------------------")
        if option == 1:
            board.add_symbol()
            game.add_player()
            game.add_enemies()
            game.add_walls()
            game.add_special_skills()
            game_turns()
            game_loop()

        elif option == 2:
            game.reset_game()
            sys.exit()
            break

        else:
            print('Invalid option, try again')
            continue

def game_loop():
    """
    Bucle principal del juego.
    """
    while True:
        print("Seleccione una dirección para mover al jugador:")
        print("1. Arriba")
        print("2. Abajo")
        print("3. Izquierda")
        print("4. Derecha")
        print ("5. Lanzar bomba")
        print("6. Diagonal arriba izq")
        print("7. Diagonal abajo izq")
        print("8. Diagonal arriba1 der")
        print("9. Diagonal abajo der")
        print("0. Salir del juego")

        choice = input("Ingrese el número de la opción: ")

        if choice == "1":
            game.move_player(1)
        elif choice == "2":
            game.move_player(2)
        elif choice == "3":
            game.move_player(3)
        elif choice == "4":
            game.move_player(4)
        elif choice == "5":
            game.drop_bomb()
        elif choice == "6":
            game.move_player(6)
        elif choice == "7":
            game.move_player(7)
        elif choice == "8":
            game.move_player(8)
        elif choice == "9":
            game.move_player(9)
        elif choice == "0":
            print("Saliendo del juego...")
            game.reset_game()
            sys.exit()
            break
        else:
            print("Opción inválida")
        game_turns()

        if game.win_game():
            break

        game.move_enemies()
        if game.check_enemy_collision():
            break


def game_turns():
    board.print_board()
