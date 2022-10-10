
from chess_game import game, board


def main():

    current_game = game.Game()

    while not current_game.end_game():
        board.draw_board(current_game.piece_list)
        print(f" au tour des {current_game.turn}")

        destination_case = None
        while destination_case is None:
            piece_to_move = None
            while piece_to_move is None:
                piece_to_move = current_game.select_piece(board.convert_alpha_to_num(input("quel piece voulez vous jouer ?").upper()))
            destination_case = current_game.select_destination(board.convert_alpha_to_num(input("ou voulez vous aller ?").upper()))
        current_game.move(piece_to_move, destination_case)
        print("\n")


main()
