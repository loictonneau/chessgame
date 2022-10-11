from chess_game import pieces


def find_piece(list: list, row: int, column: int) -> pieces.Piece:
    """trouve une piece en fonction de ces coordonnées"""

    for piece in list:

        if piece.position == [row, column]:

            return piece


def comparaison_list(action: str, list_1: list, list_2: list) -> list:
    """donne sois l'intersection sois la difference de deux liste"""

    difference_list = []
    if action == "intersection":

        difference_list = [value for value in list_1 if value in list_2]

    if action == "difference":

        difference_list = [value for value in list_1 if value not in list_2]

    return difference_list
