from chess_game import pieces, utils, constants


class Bishop(pieces.Piece):

    def __init__(self, piece_type: str, color: str, position: list):
        super().__init__(piece_type, color, position)

    def get_available_moves(self, list_pieces: list[pieces.Piece]) -> tuple:
        """
        cree un tuple contenant :
            une liste des coordonnée de tous les coups possibles du fou \n
            coup_possible[coordonné[ligne,colonne]] \n
            une liste des coordonnée de tous les coups possible du fou ordonnée par direction \n
            coups_possibles[direction[coordonnée[ligne,colonne]]]
        """

        self.clear_available_moves()
        row = self.position[0]
        column = self.position[1]

        # ajoute les cases de la diagonal haut gauche du fou jusqua ce qu'une autre piece ne sois trouvée

        if row - 1 >= 0 and column - 1 >= 0:

            available_moves_by_direction = []
            for row_down in range(row - 1, -1, -1):

                for column_left in range(column - 1, -1, -1):

                    if abs(row_down - row) == abs(column_left - column):

                        piece = utils.find_piece(list_pieces, row_down, column_left)
                        if self.color != piece.color:

                            self.available_moves.append([row_down, column_left])
                            available_moves_by_direction.append([row_down, column])

            self.available_moves_by_direction.append(available_moves_by_direction)

        # ajoute les cases de la diagonal haut droite du fou jusqua ce qu'une autre piece ne sois trouvée

        if row - 1 >= 0 and column + 1 < constants.column:

            available_moves_by_direction = []
            for row_down in range(row - 1, -1, -1):

                for column_rignt in range(column + 1, constants.column):

                    if abs(row_down - row) == abs(column_rignt - column):

                        piece = utils.find_piece(list_pieces, row_down, column_rignt)
                        if self.color != piece.color:

                            self.available_moves.append([row_down, column_rignt])
                            available_moves_by_direction.append([row_down, column])

            self.available_moves_by_direction.append(available_moves_by_direction)

        # ajoute les cases de la diagonal bas droite du fou jusqua ce qu'une autre piece ne sois trouvée

        if row + 1 < constants.row and column + 1 < constants.column:

            available_moves_by_direction = []
            for row_up in range(row + 1, constants.row):

                for column_rignt in range(column + 1, constants.column):

                    if abs(row_up - row) == abs(column_rignt - column):

                        piece = utils.find_piece(list_pieces, row_up, column_rignt)
                        if self.color != piece.color:

                            self.available_moves.append([row_up, column_rignt])
                            available_moves_by_direction.append([row_up, column])

            self.available_moves_by_direction.append(available_moves_by_direction)

        # ajoute les cases de la diagonal bas gauche du fou jusqua ce qu'une autre piece ne sois trouvée

        if row + 1 < constants.row and column - 1 >= 0:

            available_moves_by_direction = []
            for row_up in range(row + 1, constants.row):

                for column_left in range(column - 1, -1, -1):

                    if abs(row_up - row) == abs(column_left - column):

                        piece = utils.find_piece(list_pieces, row_up, column_left)
                        if self.color != piece.color:

                            self.available_moves.append([row_up, column_left])
                            available_moves_by_direction.append([row_up, column])

            self.available_moves_by_direction.append(available_moves_by_direction)

        return self.available_moves, self.available_moves_by_direction
