import itertools
from chess_game import utils, pieces, pawn, rook, knight, bishop, queen, king, board, constants


class Game:

    def __init__(self):
        """cree un liste contenant tout les pieces et les cases vides"""
        self.turn = "white"
        self.selected = None
        self.valid_moves = []
        self.piece_list = []
        self.black_pieces_left = 16
        self.white_pieces_left = 16

        """
        for each_row in range(constants.column):
            for each_case in range(constants.row):
                if each_row == 0 and each_case == 0:
                    self.piece_list.append(king.King("king", "black", [each_row, each_case]))
                elif each_row == 7 and each_case == 7:
                    self.piece_list.append(king.King("king", "white", [each_row, each_case]))
                elif each_row == 6 and each_case == 1:
                    self.piece_list.append(rook.Rook("rook", "white", [each_row, each_case]))
                elif each_row == 7 and each_case == 1:
                    self.piece_list.append(rook.Rook("rook", "white", [each_row, each_case]))
                else:
                    self.piece_list.append(pieces.Piece(None, None, [each_row, each_case]))
        """

        # place les piece en debut de partie

        for each_row, each_case in itertools.product(range(constants.column), range(constants.row)):
            if each_case in [0, 7]:
                if each_row == 0:

                    self.piece_list.append(rook.Rook("rook", "black", [each_row, each_case]))

            elif each_case in [1, 6]:
                if each_row == 0:

                    self.piece_list.append(knight.Knight("knight", "black", [each_row, each_case]))

            elif each_case in [2, 5]:
                if each_row == 0:

                    self.piece_list.append(bishop.Bishop("bishop", "black", [each_row, each_case]))

            elif each_case == 3:
                if each_row == 0:

                    self.piece_list.append(queen.Queen("queen", "black", [each_row, each_case]))

            elif each_case == 4:
                if each_row == 0:

                    self.piece_list.append(king.King("king", "black", [each_row, each_case]))

            # placement des pions noirs

            if each_row == 1:

                self.piece_list.append(pawn.Pawn("pawn", "black", [each_row, each_case]))

            # placement des cases vides

            if 2 <= each_row <= 5:

                self.piece_list.append(pieces.Piece(None, None, [each_row, each_case]))

            # placement des pions blancs

            if each_row == 6:

                self.piece_list.append(pawn.Pawn("pawn", "white", [each_row, each_case]))

                # placement des pieces blanches

            if each_row == 7:

                if each_case in [0, 7]:

                    self.piece_list.append(rook.Rook("rook", "white", [each_row, each_case]))

                elif each_case in [1, 6]:

                    self.piece_list.append(knight.Knight("knight", "white", [each_row, each_case]))

                elif each_case in [2, 5]:

                    self.piece_list.append(bishop.Bishop("bishop", "white", [each_row, each_case]))

                elif each_case == 3:

                    self.piece_list.append(queen.Queen("queen", "white", [each_row, each_case]))

                elif each_case == 4:

                    self.piece_list.append(king.King("king", "white", [each_row, each_case]))

    # bouge les pieces

    def select_piece(self, position: list[int, int]) -> (pieces.Piece, None):
        """selectionne une pièce en fonction de sa position et montre ces coups possibles"""

        if position[0] not in range(constants.row) or position[1] not in range(constants.column) or len(position) != 2:

            print("coordonnées non valide")

        else:

            piece = utils.find_piece(self.piece_list, position[0], position[1])

            if piece.type is None:

                return print("pas de piece a l'endroit choisie")

            elif self.turn != piece.color:

                return print("cette piece ne vous appartient pas")

            elif len(piece.get_available_moves(self.piece_list)[0]) <= 0:

                return print("cette piece en peut pas bouger")

            else:

                self.selected = piece
                self.valid_moves = self.selected.get_available_moves(self.piece_list)[0]
                board.convert_num_to_alpha(self.selected)

                return piece

    def select_destination(self, destination: list[list[int, int]]) -> (pieces.Piece, None):
        """selectionne une case vide"""

        if destination[0] not in range(constants.row)\
                or destination[1] not in range(constants.column) \
                or len(destination) != 2:

            return print("coordonnées non valide")

        elif destination not in self.valid_moves:

            return print("vous ne pouvez pas bouger cette piece ici ")

        else:

            return destination

    def move(self, piece: pieces.Piece, destination: list[int, int]) -> bool:
        """deplace la piece"""

        piece_to_remove = utils.find_piece(self.piece_list, destination[0], destination[1])

        # retire la piece mangé

        if piece_to_remove.color is not None:

            self.piece_die(piece_to_remove)
            piece_to_remove.type = None
            piece_to_remove.color = None

        # realise le mouvement

        piece_to_remove.position = piece.position
        piece.position = destination
        piece.first_move_done()
        self.change_turn()
        return True

    # fin d'un tour

    def change_turn(self):
        """passe a joueur suivant"""

        self.turn = "black" if self.turn == "white" else "white"

    def piece_die(self, piece_to_remove: pieces.Piece):
        """enleve 1 au compte restant du nombre de pieces"""

        # retire une piece au joueur noir

        if piece_to_remove.color == "black":

            self.black_pieces_left -= 1
            if self.black_pieces_left == 1:

                print(f"\nles noirs n'ont plus qu'une piece en jeu")

            elif self.black_pieces_left > 1:

                print(f"\nles noirs n'ont plus que {self.black_pieces_left} pieces en jeu")

            print(f"les blancs ont toujours {self.white_pieces_left} pieces en jeu")

        # retire une piece au joueur blanc

        elif piece_to_remove.color == "white":

            self.white_pieces_left -= 1
            if self.black_pieces_left == 1:

                print(f"\nles blancs n'ont plus qu'une piece en jeu")

            elif self.black_pieces_left > 1:

                print(f"\nles blancs n'ont plus que {self.white_pieces_left} pieces en jeu")

            print(f"les noirs ont toujours {self.black_pieces_left} pieces en jeu")

    # mise en echec

    def find_king(self):
        """trouve le roi d'un joueur"""

        for piece in self.piece_list:

            if piece.type == "king" and piece.color == self.turn:

                return piece

    def get_enemies_available_moves(self) -> list[list[int, int]]:
        """cree une liste avec tout les coups possibles de toutes les pieces enemies"""

        enemies_available_moves = []
        for piece in self.piece_list:

            if piece.color != self.turn and piece.type is not None:

                enemie_available_moves = piece.get_available_moves(self.piece_list)[0]
                enemies_available_moves.extend(iter(enemie_available_moves))
        return enemies_available_moves

    def get_all_possible_moves(self) -> dict[(list[int, int]), pieces.Piece]:
        """cree un dictionnaire avec tout les coups possibles associé a leur piece sauf celle du roi"""
        all_possible_moves = {}

        for piece in self.piece_list:

            if piece.color == self.turn and piece.type != "king":

                possible_moves = piece.get_available_moves(self.piece_list)[0]
                for possible_move in possible_moves:

                    all_possible_moves[possible_move] = piece

            return all_possible_moves

    def get_threatening_enemies(self) -> list[pieces.Piece]:
        """cree une liste avec les pieces metant le roi en echec"""
        player_king = self.find_king()
        threatening_enemies = []

        for piece in self.piece_list:

            if piece.color != self.turn and piece.type is not None:

                enemie_available_moves = piece.get_available_moves(self.piece_list)[0]
                threatening_enemies.extend(
                    piece for enemie_available_move in enemie_available_moves
                    if player_king.position in enemie_available_move
                )

        return threatening_enemies

    def defence_by_capturing(self):
        """capture la pièce qui donne l'échec"""

        pass

    def defence_by_moving(self):
        """déplacer hors de la menace son roi"""

        pass

    def defence_by_blocking(self):
        """le protéger en interposant une autre pièce pour parer cette menace"""

        pass

    def check(self):
        """verifie l'echec """

    # fin du jeu

    def checkmate(self):
        """verifie l'echec et mate"""

        # king = self.find_king()
        # king_possible_moves = king.get_available_moves(self.piece_list)
        # enemies_available_moves = self.get_enemies_available_moves()
        # all_available_moves = self.get_all_possible_moves()
        # king_available_moves = comparaison_list("difference", king_possible_moves, enemies_available_moves)
        # LE COUP QUE LE ROI PEUT FAIRE HORS D4ATTEINTE DES PIECE ENEMIE
        # meeting_case = comparaison_list("intersection", king_possible_moves, enemies_available_moves)
        # possible_move_to_defend = comparaison_list("inetersection", meeting_case,all_available_moves)
        # le protéger en interposant une autre pièce pour parer cette menace
        # if len(king_available_moves) == 0 and len(king_possible_moves) != 0 and len(possible_move_to_defend) == 0:
        #     return True
        # return False
        pass

    def end_game(self) -> bool:
        """met fin a la partie"""

        if self.checkmate():

            print("CHEKMATE")
            if self.turn == "white":

                print("Black wins")
            else:

                print("White wins")

            return True
