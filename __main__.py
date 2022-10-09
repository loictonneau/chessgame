
from chess_game import game,tools


def main():

    current_game = game.Game()
    tools.draw_board(current_game.piece_list)
    print(f"au tour des {current_game.turn}")
    choice_piece = current_game.select(tools.convert_coordonate(input("quel piece voulez vous jouer ?").upper()))



main()

