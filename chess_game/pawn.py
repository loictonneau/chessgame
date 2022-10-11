from chess_game import pieces, utils, constants


class Pawn(pieces.Piece):

    def __init__(self, piece_type: str, color: str, position: list):
        super().__init__(piece_type, color, position)
        self.first_move = True

    def get_available_moves(self, list_pieces: list) -> tuple:
        """
        cree un tuple contenant :
            une liste des coordonnée de tous les coups possibles du pion \n
            coup_possible[coordonné[ligne,colonne]] \n
            une liste des coordonnée de tous les coups possible du pion ordonnée par direction \n
            coups_possibles[direction[coordonnée[ligne,colonne]]]
        """

        self.clear_available_moves()
        row = self.position[0]
        column = self.position[1]

        # si le pion est blanc il avance en retranchant 1 au ligne

        if self.color == "white":

            # avance d'une case si elle est vide

            if row - 1 >= 0:

                available_moves_by_direction = []
                piece = utils.find_piece(list_pieces, row - 1, column)
                if piece.type is None:

                    self.available_moves.append([row - 1, column])
                    available_moves_by_direction.append([row - 1, column])

                    # avance de deux case si c'est son premier coup et que cette case est vide

                    if self.first_move:

                        piece = utils.find_piece(list_pieces, row - 2, column)
                        if piece.type is None:

                            self.available_moves.append([row - 2, column])
                            available_moves_by_direction.append([row - 2, column])

                self.available_moves_by_direction.append(available_moves_by_direction)

                # mange une piece adverse en diagonal ( version gauche )

                if column - 1 >= 0:

                    piece = utils.find_piece(list_pieces, row - 1, column - 1)
                    if piece.type is not None:

                        if self.color is not piece.color:

                            self.available_moves.append([row - 1, column - 1])

                # mange une piece adverse en diagonal ( version droite )

                if column + 1 < constants.column:

                    piece = utils.find_piece(list_pieces, row - 1, column + 1)
                    if piece.type is not None:

                        if self.color is not piece.color:

                            self.available_moves.append([row - 1, column + 1])

        # si le pion est noir il avance en ajoutant 1 au ligne

        if self.color == "black":

            # avance d'une case si elle est vide

            if row + 1 < constants.row:

                available_moves_by_direction = []
                piece = utils.find_piece(list_pieces, row + 1, column)
                if piece.type is None:

                    self.available_moves.append([row + 1, column])
                    available_moves_by_direction.append([row + 1, column])

                    # avance de deux case si c'est son premier coup et que cette case est vide

                    if self.first_move:

                        piece = utils.find_piece(list_pieces, row + 2, column)
                        if piece.type is None:

                            self.available_moves.append([row + 2, column])
                            available_moves_by_direction.append([row + 2, column])
                self.available_moves_by_direction.append(available_moves_by_direction)

                # mange une piece adverse en diagonal ( version gauche )

                if column - 1 >= 0:

                    piece = utils.find_piece(list_pieces, row + 1, column - 1)
                    if piece.type is not None:

                        if self.color is not piece.color:

                            self.available_moves.append([row + 1, column - 1])

                # mange une piece adverse en diagonal ( version droite )

                if column + 1 < constants.column:

                    piece = utils.find_piece(list_pieces, row + 1, column + 1)
                    if piece.type is not None:

                        if self.color is not piece.color:

                            self.available_moves.append([row + 1, column + 1])

        return self.available_moves, self.available_moves_by_direction
