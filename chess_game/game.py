from chess_game import constants, pieces, pawn, rook, knight, bishop, queen, king, tools


class Game:

    def __init__(self):  # creer un liste contenant tout les pieces et la cas vide
        self.turn = "white"
        self.selected = None
        self.valid_moves = []
        self.piece_list = []
        self.black_pieces_left = 16
        self.white_pieces_left = 16

        for each_row in range(constants.column):
            for each_case in range(constants.row):

                # place les piece en debut de partie
                if each_row == 0:
                    if each_case == 0 or each_case == 7:
                        self.piece_list.append(rook.Rook("rook", "black", [each_row,each_case]))
                    elif each_case == 1 or each_case == 6:
                        self.piece_list.append(knight.Knight("knight", "black", [each_row,each_case]))
                    elif each_case == 2 or each_case == 5:
                        self.piece_list.append(bishop.Bishop("bishop", "black", [each_row,each_case]))
                    elif each_case == 3:
                        self.piece_list.append(queen.Queen("queen", "black", [each_row,each_case]))
                    elif each_case == 4:
                        self.piece_list.append(king.King("king", "black", [each_row,each_case]))

                if each_row == 1:
                    self.piece_list.append(pawn.Pawn("pawn", "black", [each_row,each_case]))

                if 2 <= each_row <= 5:
                    self.piece_list.append(pieces.Piece(None, None, [each_row,each_case]))

                if each_row == 6:
                    self.piece_list.append(pawn.Pawn("pawn", "white", [each_row,each_case]))

                if each_row == 7:
                    if each_case == 0 or each_case == 7:
                        self.piece_list.append(rook.Rook("rook", "white", [each_row,each_case]))
                    elif each_case == 1 or each_case == 6:
                        self.piece_list.append(knight.Knight("knight", "white", [each_row,each_case]))
                    elif each_case == 2 or each_case == 5:
                        self.piece_list.append(bishop.Bishop("bishop", "white", [each_row,each_case]))
                    elif each_case == 3:
                        self.piece_list.append(queen.Queen("queen", "white", [each_row,each_case]))
                    elif each_case == 4:
                        self.piece_list.append(king.King("king", "white", [each_row,each_case]))


    def select_piece(self, position):  # selectionne une pièce en fonction de a position et montre ces coups possibles
        if not (position[0] in range(0,constants.row) and position[1] in range(0,constants.column)) or len(position) != 2:
            return print("coordonnées non valide")

        else:
            piece = tools.find_piece(self.piece_list, position[0], position[1])

            if piece.type is None:
                return print("pas de piece a l'endroit choisie")

            elif self.turn != piece.color:
                return print("cette piece ne vous appartient pas")

            elif len(piece.get_available_moves(self.piece_list)) <= 0:
                return print("cette piece en peut pas bouger")

            else:
                self.selected = piece
                self.valid_moves = piece.get_available_moves(self.piece_list)
                tools.convert_num_to_alpha(self.selected)
                return piece

    def select_destination(self, destination):  # selectionne une case vide
        if not (destination[0] in range(0, constants.row) and destination[1] in range(0, constants.column)) or len(destination) != 2:
            return print("coordonnées non valide")

        elif destination not in self.valid_moves :
            return print("vous ne pouvez pas bouger cette piece ici ")
        else:
            return destination

    def first_move_done(self,piece):  # change la possibilité des coups speciaux lié au premier deplacement
        if piece.type in ("pawn","rook","king"):
            piece.first_move = False

    def change_turn(self):  # passe a joueur suivant
        if self.turn == "white":
            self.turn = "black"
        else:
            self.turn = "white"

    def piece_die(self,piece_removed): #  enleve 1 au compte restant du nombre de pieces
        if piece_removed.color == "black":
            self.black_pieces_left -= 1
        elif piece_removed.color == "white":
            self.white_pieces_left -= 1

    def move(self,piece,destination):  # deplace la piece
        piece_to_remove = tools.find_piece(self.piece_list,destination[0],destination[1])
        if piece_to_remove.color is not None:
            self.piece_die(piece_to_remove)
            piece_to_remove.type = None
            piece_to_remove.color = None
        piece_to_remove.position = piece.position
        piece.position = destination

        self.first_move_done(piece)
        self.change_turn()
