from chess_game import pieces, utils, constants


class Knight(pieces.Piece):

    def __init__(self, piece_type: str, color: str, position: list[int, int]):
        super().__init__(piece_type, color, position)

    def get_available_moves(self, list_pieces: list[pieces.Piece]) \
            -> tuple[list[list[int, int]], list[list[list[int, int]]]]:
        """
        cree un tuple contenant :
            une liste des coordonnée de tous les coups possibles du cavalier \n
            coup_possible[coordonné[ligne,colonne]] \n
            une liste des coordonnée de tous les coups possible du cavalier ordonnée par direction \n
            coups_possibles[direction[coordonnée[ligne,colonne]]]
        """

        self.clear_available_moves()
        row = self.position[0]
        column = self.position[1]

    # le cavalier peut bouger sur 8 case differente

        # 2 gauche 1 haut

        if row - 1 >= 0 and column - 2 >= 0:

            available_moves_by_direction = []
            piece = utils.find_piece(list_pieces, row - 1, column - 2)
            if self.color is not piece.color:

                self.available_moves.append([row - 1, column - 2])
                available_moves_by_direction.append([row - 1, column - 2])

            self.available_moves_by_direction.append(available_moves_by_direction)

        # 2 haut 1 gauche

        if row - 2 >= 0 and column - 1 >= 0:

            available_moves_by_direction = []
            piece = utils.find_piece(list_pieces, row - 2, column - 1)
            if self.color is not piece.color:

                self.available_moves.append([row - 2, column - 1])
                available_moves_by_direction.append([row - 2, column - 1])

            self.available_moves_by_direction.append(available_moves_by_direction)

        # 2 haut 1 droite

        if row - 2 >= 0 and column + 1 < constants.column:

            available_moves_by_direction = []
            piece = utils.find_piece(list_pieces, row - 2, column + 1)
            if self.color is not piece.color:

                self.available_moves.append([row - 2, column + 1])
                available_moves_by_direction.append([row - 2, column - 1])

            self.available_moves_by_direction.append(available_moves_by_direction)

        # 2 droite 1 haut

        if row - 1 >= 0 and column + 2 < constants.column:

            available_moves_by_direction = []
            piece = utils.find_piece(list_pieces, row - 1, column + 2)
            if self.color is not piece.color:

                self.available_moves.append([row - 1, column + 2])
                available_moves_by_direction.append([row - 1, column + 2])

            self.available_moves_by_direction.append(available_moves_by_direction)

        # 2 droite 1 bas

        if row + 1 < constants.row and column + 2 < constants.column:

            available_moves_by_direction = []
            piece = utils.find_piece(list_pieces, row + 1, column + 2)
            if self.color is not piece.color:

                self.available_moves.append([row + 1, column + 2])
                available_moves_by_direction.append([row + 1, column + 2])

            self.available_moves_by_direction.append(available_moves_by_direction)

        # 2 bas 1 droite

        if row + 2 < constants.row and column + 1 < constants.column:

            available_moves_by_direction = []
            piece = utils.find_piece(list_pieces, row + 2, column + 1)
            if self.color is not piece.color:

                self.available_moves.append([row + 2, column + 1])
                available_moves_by_direction.append([row + 2, column + 1])

            self.available_moves_by_direction.append(available_moves_by_direction)

        # 2 bas 1 gauche

        if row + 2 < constants.row and column - 1 >= 0:

            available_moves_by_direction = []
            piece = utils.find_piece(list_pieces, row + 2, column - 1)
            if self.color is not piece.color:

                self.available_moves.append([row + 2, column - 1])
                available_moves_by_direction.append([row + 2, column - 1])

            self.available_moves_by_direction.append(available_moves_by_direction)

        # 2 gauche 1 bas

        if row + 1 < constants.row and column - 2 >= 0:

            available_moves_by_direction = []
            piece = utils.find_piece(list_pieces, row + 1, column - 2)
            if self.color is not piece.color:

                self.available_moves.append([row + 1, column - 2])
                available_moves_by_direction.append([row + 1, column - 2])

            self.available_moves_by_direction.append(available_moves_by_direction)

        return self.available_moves, self.available_moves_by_direction
