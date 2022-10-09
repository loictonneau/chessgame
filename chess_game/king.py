from . import pieces, constants, tools


class King(pieces.Piece):

    def __init__(self, piece_type, color, position):
        super().__init__(piece_type, color, position)
        self.first_move = True

    def get_available_moves(self, list_pieces):  # creer une liste avec tout les coups possibles du pion
        self.clear_available_moves()
        row = self.position[0]
        column = self.position[1]

        if row - 1 >= 0:  # avance d'une case vers le bas
            piece = tools.find_piece(list_pieces, row - 1, column)
            if piece.type is None:
                self.available_moves.append([row - 1, column])

        if row + 1 < constants.row - 1:  # avance d'une case vers le haut
            piece = tools.find_piece(list_pieces, row + 1, column)
            if piece.type is None:
                self.available_moves.append([row + 1, column])

        if column - 1 >= 0:  # avance d'une case sur la gauche
            piece = tools.find_piece(list_pieces, row, column - 1)
            if piece.type is None:
                self.available_moves.append([row, column - 1])

        if column + 1 < constants.column - 1:  # avance d'une case sur la droite
            piece = tools.find_piece(list_pieces, row, column + 1)
            if piece.type is None:
                self.available_moves.append([row, column + 1])

        if row - 1 >= 0 and column + 1 < constants.column - 1:  # avance d'une case sur le diagonal S.E.
            piece = tools.find_piece(list_pieces, row - 1, column + 1)
            if piece.type is None:
                self.available_moves.append([row - 1, column + 1])

        if row - 1 >= 0 and column - 1 >= 0:  # avance d'une case sur le diagonal S.O.
            piece = tools.find_piece(list_pieces, row - 1, column - 1)
            if piece.type is None:
                self.available_moves.append([row - 1, column - 1])

        if row + 1 < constants.row - 1 and column + 1 < constants.column - 1:  # avance d'une case sur le diagonal N.E.
            piece = tools.find_piece(list_pieces, row - 1, column + 1)
            if piece.type is None:
                self.available_moves.append([row - 1, column + 1])

        if row + 1 < constants.row - 1 and column - 1 >= 0:  # avance d'une case sur le diagonal N.O.
            piece = tools.find_piece(list_pieces, row - 1, column - 1)
            if piece.type is None:
                self.available_moves.append([row - 1, column - 1])

        return self.available_moves
