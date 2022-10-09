
from chess_game import game,tools


def main():

    current_game = game.Game()
    tools.draw_board(current_game.piece_list)
    print(f"au tour des {current_game.turn}")

    piece_to_move = None
    while piece_to_move is None:
        piece_to_move = current_game.select_piece(tools.convert_alpha_to_num(input("quel piece voulez vous jouer ?").upper()))

    destination_case = None
    while destination_case is None:
        destination_case = current_game.select_destination(tools.convert_alpha_to_num(input("ou voulez vous aller ?").upper()))



main()

