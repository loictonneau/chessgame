from . import pieces, constants, game


class Bishop(pieces.Piece):

    def __init__(self, piece_type, color, position):
        super().__init__(piece_type, color, position)

    def get_available_moves(self, list_pieces):  # cree une liste avec tout les coups possibles du cavalier
        self.clear_available_moves()
        row = self.position[0]
        column = self.position[1]

        if row - 1 >= 0 and column - 1 >= 0:  # ajoute les cases de la diagonal haut gauche du fou tant qu'aucune autre piece n'est trouvée
            for row_down in range(row - 1, -1, -1):
                for column_left in range(column - 1, -1, -1):
                    if abs(row_down - row) == abs(column_left - column):
                        piece = game.find_piece(list_pieces, row_down, column_left)
                        if self.color != piece.color:
                            self.available_moves.append([row_down, column_left])

        if row - 1 >= 0 and column + 1 < constants.column:  # ajoute les cases de la diagonal haut droite du fou tant qu'aucune autre piece n'est trouvée
            for row_down in range(row - 1, -1, -1):
                for column_rignt in range(column + 1, constants.column):
                    if abs(row_down - row) == abs(column_rignt - column):
                        piece = game.find_piece(list_pieces, row_down, column_rignt)
                        if self.color != piece.color:
                            self.available_moves.append([row_down, column_rignt])

        if row + 1 < constants.row and column + 1 < constants.column:  # ajoute les cases de la diagonal bas droite du fou tant qu'aucune autre piece n'est trouvée
            for row_up in range(row + 1, constants.row):
                for column_rignt in range(column + 1, constants.column):
                    if abs(row_up - row) == abs(column_rignt - column):
                        piece = game.find_piece(list_pieces, row_up, column_rignt)
                        if self.color != piece.color:
                            self.available_moves.append([row_up, column_rignt])

        if row + 1 < constants.row and column - 1 >= 0:  # ajoute les cases de la diagonal bas gauche du fou tant qu'aucune autre piece n'est trouvée
            for row_up in range(row + 1, constants.row):
                for column_left in range(column - 1, -1, -1):
                    if abs(row_up - row) == abs(column_left - column):
                        piece = game.find_piece(list_pieces, row_up, column_left)
                        if self.color != piece.color:
                            self.available_moves.append([row_up, column_left])

        return self.available_moves
