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
    # letter_ = (0, 1, 2, 3, 4, 5, 6, 7)
    print("    1    2    3    4    5    6    7    8 ")
    # print("    0    1    2    3    4    5    6    7 ")
    for each_line in range(len(board)):
        print(str(letter[each_line]) + str(board[each_line]))


def convert_coordonate(position):  # permet de passer des coordonnées alphanumerique a des coordonnées numeriques
    letter = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
    position = list(position)
    position[0] = letter.get(position[0])
    position[1] = int(position[1]) - 1
    return position


def print_available_moves(piece):  # permet de passer des coordonnées numerique a des coordonnées alphanumerique
    available_moves = []
    for available_move in piece.available_moves:
        available_move = list(available_move)
        if available_move[0] == 0:
            available_move[0] = "A"
        if available_move[0] == 1:
            available_move[0] = "B"
        if available_move[0] == 2:
            available_move[0] = "C"
        if available_move[0] == 3:
            available_move[0] = "D"
        if available_move[0] == 4:
            available_move[0] = "E"
        if available_move[0] == 5:
            available_move[0] = "F"
        if available_move[0] == 6:
            available_move[0] = "G"
        if available_move[0] == 7:
            available_move[0] = "H"
        available_move[1] = str(available_move[1] + 1)
        available_move = available_move[0] + available_move[1]
        available_moves.append(available_move)
    print(f"les case disponible sont {available_moves}")


def find_piece(list_pieces, row, colum):  # trouve une piece en fonction de ces coordonnées
    for piece in list_pieces:
        if piece.position == [row, colum]:
            return piece
