
from . import pieces, constants, tools


class Knight(pieces.Piece):

    def __init__(self, piece_type, color, position):
        super().__init__(piece_type, color, position)

    def get_available_moves(self, list_pieces):  # creer une liste avec tout les coups possibles du cavalier
        self.clear_available_moves()
        row = self.position[0]
        column = self.position[1]

        # le cavalier peut bouger sur 8 case differente
        if row - 2 >= 0 and column + 1 < constants.column - 1:
            piece = tools.find_piece(list_pieces, row - 2, column + 1)
            if self.color is not piece.color:
                self.available_moves.append([row - 2, column + 1])

        if row - 2 >= 0 and column - 1 >= 0:
            piece = tools.find_piece(list_pieces, row - 2, column - 1)
            if self.color is not piece.color:
                self.available_moves.append([row - 2, column - 1])

        if row + 2 < constants.row - 1 and column + 1 < constants.column - 1:
            piece = tools.find_piece(list_pieces, row + 2, column + 1)
            if self.color is not piece.color:
                self.available_moves.append([row + 2, column + 1])

        if row + 2 < constants.row - 1 and column - 1 >= 0:
            piece = tools.find_piece(list_pieces, row + 2, column - 1)
            if self.color is not piece.color:
                self.available_moves.append([row + 2, column - 1])

        if row - 1 >= 0 and column + 2 < constants.column - 1:
            piece = tools.find_piece(list_pieces, row - 1, column + 2)
            if self.color is not piece.color:
                self.available_moves.append([row - 1, column + 2])

        if row - 1 >= 0 and column - 2 >= 0:
            piece = tools.find_piece(list_pieces, row - 1, column - 2)
            if self.color is not piece.color:
                self.available_moves.append([row - 1, column - 2])

        if row + 1 < constants.row - 1 and column + 2 < constants.column - 1:
            piece = tools.find_piece(list_pieces, row + 1, column + 2)
            if self.color is not piece.color:
                self.available_moves.append([row + 1, column + 2])

        if row + 1 < constants.row - 1 and column - 2 >= 0:
            piece = tools.find_piece(list_pieces, row + 1, column - 2)
            if self.color is not piece.color:
                self.available_moves.append([row + 1, column - 2])

        return self.available_moves
