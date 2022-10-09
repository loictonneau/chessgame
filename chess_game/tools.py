from chess_game import constants


def draw_board(list):  # affiche les pieces sur un echequier

    board = []
    for each_rows in range(constants.column):
        row = []
        for each_case in range(constants.row):
            for piece in list:
                if piece.position[0] == each_rows and piece.position[1] == each_case:
                    if piece.type is None:  # case vide
                        row.append(" ")
                        break

                    elif piece.color == "black":  # les pions noirs sont en minuscule
                        if piece.type == "pawn":
                            row.append("p")
                            break
                        elif piece.type == "rook":
                            row.append("t")
                            break
                        elif piece.type == "knight":
                            row.append("c")
                            break
                        elif piece.type == "bishop":
                            row.append("f")
                            break
                        elif piece.type == "queen":
                            row.append("d")
                            break
                        elif piece.type == "king":
                            row.append("r")
                            break

                    elif piece.color == "white":  # les pions blancs sont en majuscule
                        if piece.type == "pawn":
                            row.append("P")
                            break
                        elif piece.type == "rook":
                            row.append("T")
                            break
                        elif piece.type == "knight":
                            row.append("C")
                            break
                        elif piece.type == "bishop":
                            row.append("F")
                            break
                        elif piece.type == "queen":
                            row.append("D")
                            break
                        elif piece.type == "king":
                            row.append("R")
                            break
        board.append(row)

    # mise en forme des bord du tableau
    letter = ("A ", "B ", "C ", "D ", "E ", "F ", "G ", "H ")
    #letter_ = (0, 1, 2, 3, 4, 5, 6, 7)
    print("    1    2    3    4    5    6    7    8 ")
    #print("    0    1    2    3    4    5    6    7 ")
    for each_line in range(len(board)):
        print(str(letter[each_line]) + str(board[each_line]))


def convert_coordonate(coordonate):  # permet de passer des coordonnées alphanumerique a des coordonnées numeriques
    letter = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
    choice_piece_list = list(coordonate)
    choice_piece_list[0] = letter.get(choice_piece_list[0])
    choice_piece_list[1] = int(choice_piece_list[1]) - 1
    return choice_piece_list



def affichage_valid_move(piece):
    valeur = []
    for values in piece.available_moves:
        values = list(values)
        if values[0] == 0:
            values[0] = "A"
        if values[0] == 1:
            values[0] = "B"
        if values[0] == 2:
            values[0] = "C"
        if values[0] == 3:
            values[0] = "D"
        if values[0] == 4:
            values[0] = "E"
        if values[0] == 5:
            values[0] = "F"
        if values[0] == 6:
            values[0] = "G"
        if values[0] == 7:
            values[0] = "H"
        values[1] = str(values[1] + 1)
        values = values[0] + values[1]
        valeur.append(values)
    print(f"les case disponible sont {valeur}")


def find_piece(list_pieces, row, colum):
    for piece in list_pieces:
        if piece.position == [row, colum]:
            return piece
