from chess_game import pieces, utils, constants


class King(pieces.Piece):

    def __init__(self, piece_type: str, color: str, position: list):
        super().__init__(piece_type, color, position)
        self.first_move = True

    def get_available_moves(self, list_pieces: list) -> tuple:
        """
        cree un tuple contenant :
            une liste des coordonnée de tous les coups possibles du roi \n
            coup_possible[coordonné[ligne,colonne]] \n
            une liste des coordonnée de tous les coups possible du roi ordonnée par direction \n
            coups_possibles[direction[coordonnée[ligne,colonne]]]
        """

        self.clear_available_moves()
        row = self.position[0]
        column = self.position[1]

        # avance d'une case sur la gauche

        if column - 1 >= 0:

            available_moves_by_direction = []
            piece = utils.find_piece(list_pieces, row, column - 1)
            if piece.color != self.color:

                self.available_moves.append([row, column - 1])
                available_moves_by_direction.append([row, column - 1])

            self.available_moves_by_direction.append(available_moves_by_direction)

        # avance d'une case sur le diagonal haut gauche

        if row - 1 >= 0 and column - 1 >= 0:

            available_moves_by_direction = []
            piece = utils.find_piece(list_pieces, row - 1, column - 1)
            if piece.color != self.color:

                self.available_moves.append([row - 1, column - 1])
                available_moves_by_direction.append([row - 1, column - 1])

            self.available_moves_by_direction.append(available_moves_by_direction)

        # avance d'une case vers le haut

        if row - 1 >= 0:

            available_moves_by_direction = []
            piece = utils.find_piece(list_pieces, row - 1, column)
            if piece.color != self.color:

                self.available_moves.append([row - 1, column])
                available_moves_by_direction.append([row - 1, column])

            self.available_moves_by_direction.append(available_moves_by_direction)

        # avance d'une case sur le diagonal haut droite

        if row - 1 >= 0 and column + 1 < constants.column:

            available_moves_by_direction = []
            piece = utils.find_piece(list_pieces, row - 1, column + 1)
            if piece.color != self.color:

                self.available_moves.append([row - 1, column + 1])
                available_moves_by_direction.append([row - 1, column + 1])

            self.available_moves_by_direction.append(available_moves_by_direction)

        # avance d'une case sur la droite

        if column + 1 < constants.column:

            available_moves_by_direction = []
            piece = utils.find_piece(list_pieces, row, column + 1)
            if piece.color != self.color:

                self.available_moves.append([row, column + 1])
                available_moves_by_direction.append([row, column + 1])

            self.available_moves_by_direction.append(available_moves_by_direction)

        # avance d'une case sur le diagonal bas droite

        if row + 1 < constants.row and column + 1 < constants.column:

            available_moves_by_direction = []
            piece = utils.find_piece(list_pieces, row + 1, column + 1)
            if piece.color != self.color:

                self.available_moves.append([row + 1, column + 1])
                available_moves_by_direction.append([row + 1, column + 1])

            self.available_moves_by_direction.append(available_moves_by_direction)

        # avance d'une case vers le bas

        if row + 1 < constants.row:

            available_moves_by_direction = []
            piece = utils.find_piece(list_pieces, row + 1, column)
            if piece.color != self.color:

                self.available_moves.append([row + 1, column])
                available_moves_by_direction.append([row + 1, column])

            self.available_moves_by_direction.append(available_moves_by_direction)

        # avance d'une case sur le diagonal bas gauche

        if row + 1 < constants.row and column - 1 >= 0:

            available_moves_by_direction = []
            piece = utils.find_piece(list_pieces, row + 1, column - 1)
            if piece.color != self.color:

                self.available_moves.append([row + 1, column - 1])
                available_moves_by_direction.append([row + 1, column - 1])

            self.available_moves_by_direction.append(available_moves_by_direction)

        return self.available_moves, self.available_moves_by_direction
