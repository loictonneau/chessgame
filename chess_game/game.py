from chess_game import constants, pieces, pawn, rook, knight, bishop, queen, king


class Game:

    def __init__(self):  # creer un liste contenant tout les pieces et la cas vide
        piece_list = []

        for each_row in range(constants.column):
            for each_case in range(constants.row):

                # place les piece en debut de partie
                if each_row == 0:
                    if each_case == 0 or each_case == 7:
                        piece_list.append(rook.Rook("rook", "white", [each_case, each_row]))
                    elif each_case == 1 or each_case == 6:
                        piece_list.append(knight.Knight("knight", "white", [each_case, each_row]))
                    elif each_case == 2 or each_case == 5:
                        piece_list.append(bishop.Bishop("bishop", "white", [each_case, each_row]))
                    elif each_case == 3:
                        piece_list.append(queen.Queen("queen", "white", [each_case, each_row]))
                    elif each_case == 4:
                        piece_list.append(king.King("king", "white", [each_case, each_row]))

                if each_row == 1:
                    piece_list.append(pawn.Pawn("pawn", "white", [each_case, each_row]))

                if 2 <= each_row <= 5:
                    piece_list.append(pieces.Piece(None, None, [each_case, each_row]))

                if each_row == 6:
                    piece_list.append(pawn.Pawn("pawn", "black", [each_case, each_row]))

                if each_row == 7:
                    if each_case == 0 or each_case == 7:
                        piece_list.append(rook.Rook("rook", "black", [each_case, each_row]))
                    elif each_case == 1 or each_case == 6:
                        piece_list.append(knight.Knight("knight", "black", [each_case, each_row]))
                    elif each_case == 2 or each_case == 5:
                        piece_list.append(bishop.Bishop("bishop", "black", [each_case, each_row]))
                    elif each_case == 3:
                        piece_list.append(queen.Queen("queen", "black", [each_case, each_row]))
                    elif each_case == 4:
                        piece_list.append(king.King("king", "black", [each_case, each_row]))

        draw_board(piece_list)


def draw_board(list):  # affiche les pieces sur un echequier

    board = []
    for each_rows in range(constants.column):
        row = []
        for each_case in range(constants.row):
            for piece in list:
                if piece.position[0] == each_case and piece.position[1] == each_rows:
                    if piece.type is None:  # case vide
                        row.append(" ")

                    elif piece.color == "black":  # les pions noirs sont en minuscule
                        if piece.type == "pawn":
                            row.append("p")
                        elif piece.type == "rook":
                            row.append("t")
                        elif piece.type == "knight":
                            row.append("c")
                        elif piece.type == "bishop":
                            row.append("f")
                        elif piece.type == "queen":
                            row.append("d")
                        elif piece.type == "king":
                            row.append("r")

                    elif piece.color == "white":  # les pions blancs sont en majuscule
                        if piece.type == "pawn":
                            row.append("P")
                        elif piece.type == "rook":
                            row.append("T")
                        elif piece.type == "knight":
                            row.append("C")
                        elif piece.type == "bishop":
                            row.append("F")
                        elif piece.type == "queen":
                            row.append("D")
                        elif piece.type == "king":
                            row.append("R")
        board.append(row)

    # mise en forme des bord du tableau
    letter = ("A ", "B ", "C ", "D ", "E ", "F ", "G ", "H ")
    print("    1    2    3    4    5    6    7    8 ")
    for each_line in range(len(board)):
        print(str(letter[each_line]) + str(board[each_line]))
