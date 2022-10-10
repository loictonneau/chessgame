from . import pieces, constants, game


class Knight(pieces.Piece):

    def __init__(self, piece_type, color, position):
        super().__init__(piece_type, color, position)

    def get_available_moves(self, list_pieces):  # cree une liste avec tout les coups possibles du cavalier
        self.clear_available_moves()
        row = self.position[0]
        column = self.position[1]

        # le cavalier peut bouger sur 8 case differente
        if row - 1 >= 0 and column - 2 >= 0:  # 2 gauche 1 haut
            piece = game.find_piece(list_pieces, row - 1, column - 2)
            if self.color is not piece.color:
                self.available_moves.append([row - 1, column - 2])

        if row - 2 >= 0 and column - 1 >= 0: # 2 haut 1 gauche
            piece = game.find_piece(list_pieces, row - 2, column - 1)
            if self.color is not piece.color:
                self.available_moves.append([row - 2, column - 1])

        if row - 2 >= 0 and column + 1 < constants.column:  # 2 haut 1 droite
            piece = game.find_piece(list_pieces, row - 2, column + 1)
            if self.color is not piece.color:
                self.available_moves.append([row - 2, column + 1])

        if row - 1 >= 0 and column + 2 < constants.column:  # 2 droite 1 haut
            piece = game.find_piece(list_pieces, row - 1, column + 2)
            if self.color is not piece.color:
                self.available_moves.append([row - 1, column + 2])

        if row + 1 < constants.row and column + 2 < constants.column:  # 2 droite 1 bas
            piece = game.find_piece(list_pieces, row + 1, column + 2)
            if self.color is not piece.color:
                self.available_moves.append([row + 1, column + 2])

        if row + 2 < constants.row and column + 1 < constants.column:  # 2 bas 1 droite
            piece = game.find_piece(list_pieces, row + 2, column + 1)
            if self.color is not piece.color:
                self.available_moves.append([row + 2, column + 1])

        if row + 2 < constants.row and column - 1 >= 0:  # 2 bas 1 gauche
            piece = game.find_piece(list_pieces, row + 2, column - 1)
            if self.color is not piece.color:
                self.available_moves.append([row + 2, column - 1])

        if row + 1 < constants.row and column - 2 >= 0:  # 2 gauche 1 bas
            piece = game.find_piece(list_pieces, row + 1, column - 2)
            if self.color is not piece.color:
                self.available_moves.append([row + 1, column - 2])

        return self.available_moves
