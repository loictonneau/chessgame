from chess_game import constants, pieces, pawn, rook, knight, bishop, queen, king, board


class Game:

    def __init__(self):  # cree un liste contenant tout les pieces et la cas vide
        self.turn = "white"
        self.selected = None
        self.valid_moves = []
        self.piece_list = []
        self.black_pieces_left = 16
        self.white_pieces_left = 16

        # for each_row in range(constants.column):
        #     for each_case in range(constants.row):
        #         if each_row == 0 and each_case == 0:
        #             self.piece_list.append(king.King("king", "black", [each_row, each_case]))
        #         elif each_row == 7 and each_case == 7:
        #             self.piece_list.append(king.King("king", "white", [each_row, each_case]))
        #         elif each_row == 6 and each_case == 1:
        #             self.piece_list.append(rook.Rook("rook", "white", [each_row, each_case]))
        #         elif each_row == 7 and each_case == 1:
        #             self.piece_list.append(rook.Rook("rook", "white", [each_row, each_case]))
        #         else:
        #             self.piece_list.append(pieces.Piece(None, None, [each_row, each_case]))

        for each_row in range(constants.column):
            for each_case in range(constants.row):
                # place les piece en debut de partie
                if each_row == 0:
                    if each_case == 0 or each_case == 7:
                        self.piece_list.append(rook.Rook("rook", "black", [each_row, each_case]))
                    elif each_case == 1 or each_case == 6:
                        self.piece_list.append(knight.Knight("knight", "black", [each_row, each_case]))
                    elif each_case == 2 or each_case == 5:
                        self.piece_list.append(bishop.Bishop("bishop", "black", [each_row, each_case]))
                    elif each_case == 3:
                        self.piece_list.append(queen.Queen("queen", "black", [each_row, each_case]))
                    elif each_case == 4:
                        self.piece_list.append(king.King("king", "black", [each_row, each_case]))

                if each_row == 1:
                    self.piece_list.append(pawn.Pawn("pawn", "black", [each_row, each_case]))

                if 2 <= each_row <= 5:
                    self.piece_list.append(pieces.Piece(None, None, [each_row, each_case]))

                if each_row == 6:
                    self.piece_list.append(pawn.Pawn("pawn", "white", [each_row, each_case]))

                if each_row == 7:
                    if each_case == 0 or each_case == 7:
                        self.piece_list.append(rook.Rook("rook", "white", [each_row, each_case]))
                    elif each_case == 1 or each_case == 6:
                        self.piece_list.append(knight.Knight("knight", "white", [each_row, each_case]))
                    elif each_case == 2 or each_case == 5:
                        self.piece_list.append(bishop.Bishop("bishop", "white", [each_row, each_case]))
                    elif each_case == 3:
                        self.piece_list.append(queen.Queen("queen", "white", [each_row, each_case]))
                    elif each_case == 4:
                        self.piece_list.append(king.King("king", "white", [each_row, each_case]))

    # bouge les pieces

    def select_piece(self, position):  # selectionne une pièce en fonction de a position et montre ces coups possibles
        if not (position[0] in range(0, constants.row) and position[1] in range(0, constants.column)) or len(
                position) != 2:
            return print("coordonnées non valide")

        else:
            piece = find_piece(self.piece_list, position[0], position[1])

            if piece.type is None:
                return print("pas de piece a l'endroit choisie")

            elif self.turn != piece.color:
                return print("cette piece ne vous appartient pas")

            elif len(piece.get_available_moves(self.piece_list)) <= 0:
                return print("cette piece en peut pas bouger")

            else:
                self.selected = piece
                self.valid_moves = piece.get_available_moves(self.piece_list)
                board.convert_num_to_alpha(self.selected)
                return piece

    def select_destination(self, destination):  # selectionne une case vide
        if not (destination[0] in range(0, constants.row) and destination[1] in range(0, constants.column)) or len(
                destination) != 2:
            return print("coordonnées non valide")

        elif destination not in self.valid_moves:
            return print("vous ne pouvez pas bouger cette piece ici ")
        else:
            return destination

    def move(self, piece, destination):  # deplace la piece
        piece_to_remove = find_piece(self.piece_list, destination[0], destination[1])
        if piece_to_remove.color is not None:
            self.piece_die(piece_to_remove)
            piece_to_remove.type = None
            piece_to_remove.color = None
        piece_to_remove.position = piece.position
        piece.position = destination

        self.first_move_done(piece)
        self.change_turn()

    def first_move_done(self, piece):  # change la possibilité des coups speciaux lié au premier deplacement
        if piece.type in ("pawn", "rook", "king"):
            piece.first_move = False

    # fin d'un tour

    def change_turn(self):  # passe a joueur suivant
        if self.turn == "white":
            self.turn = "black"
        else:
            self.turn = "white"

    def piece_die(self, piece_removed):  # enleve 1 au compte restant du nombre de pieces
        print("\n")
        if piece_removed.color == "black":
            self.black_pieces_left -= 1
            if self.black_pieces_left == 1:
                print(f"les noirs n'ont plus qu'une piece en jeu")
            elif self.black_pieces_left > 1:
                print(f"les noirs n'ont plus que {self.black_pieces_left} pieces en jeu")
            print(f"les blancs ont toujours {self.white_pieces_left} pieces en jeu")

        elif piece_removed.color == "white":
            self.white_pieces_left -= 1
            if self.black_pieces_left == 1:
                print(f"les blancs n'ont plus qu'une piece en jeu")
            elif self.black_pieces_left > 1:
                print(f"les blancs n'ont plus que {self.white_pieces_left} pieces en jeu")
            print(f"les noirs ont toujours {self.black_pieces_left} pieces en jeu")

    # fin du jeu
    def find_king(self):  # trouve le roi d'un joueur
        for piece in self.piece_list:
            if piece.type == "king" and piece.color == self.turn:
                return piece

    def get_enemies_available_moves(self):  # cree une liste avec tout les coups possibles de toutes les pieces enemies
        enemies_available_moves = []
        for piece in self.piece_list:
            if piece.color != self.turn and piece.type is not None:
                enemie_available_moves = piece.get_available_moves(self.piece_list)
                for enemie_available_move in enemie_available_moves:
                    enemies_available_moves.append(enemie_available_move)

        return enemies_available_moves

    def get_all_possible_moves(
            self):  # cree une liste avec tout les coups possibles de toutes les pieces allié sauf le roi
        all_possible_moves = []
        for piece in self.piece_list:
            if piece.color == self.turn and piece.type != "king":
                possible_moves = piece.get_available_moves(self.piece_list)
                for possible_move in possible_moves:
                    all_possible_moves.append(possible_move)

            return all_possible_moves

    def checkmate(self):  # verifie l'echec et mate
        king = self.find_king()
        king_possible_moves = king.get_available_moves(self.piece_list)
        enemies_available_moves = self.get_enemies_available_moves()
        all_available_moves = self.get_all_possible_moves()
        king_available_moves = comparaison_list("difference", king_possible_moves, enemies_available_moves)
        meeting_case = comparaison_list("intersection", king_possible_moves, enemies_available_moves)
        possible_move_to_defend = comparaison_list("inetersection", meeting_case,all_available_moves)
        if len(king_available_moves) == 0 and len(king_possible_moves) != 0 and len(possible_move_to_defend) == 0:
            return True
        return False

    def end_game(self):  # fin de la partie
        if self.checkmate():
            if self.turn == "white":
                print("Black wins")
                return True
            else:
                print("White wins")
                return True


# utilitaire

def find_piece(list, row, column):  # trouve une piece en fonction de ces coordonnées
    for piece in list:
        if piece.position == [row, column]:
            return piece


def comparaison_list(action, list_1, list_2):
    difference_list = []
    if action == "intersection":
        difference_list = [value for value in list_1 if value in list_2]
    if action == "difference":
        difference_list = [value for value in list_1 if value not in list_2]
    return difference_list
