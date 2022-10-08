from . import pieces,constants


class Bishop(pieces.Piece):

    def __init__(self, piece_type, color, position):
        super().__init__(piece_type, color, position)

    def get_available_moves(self, list_pieces):  # creer une liste avec tout les coups possibles du cavalier
        self.clear_available_moves()
        row = self.position[0]
        column = self.position[1]

        if row + 1 < constants.row + 1 and column + 1 < constants.column + 1:  # ajoute les cases de la diagonal N.E. du fou tant qu'aucune autre piece n'est trouvée
            for row_up in range(row + 1, constants.row):
                for column_rignt in range(column + 1, constants.column):
                    if row_up == column_rignt:
                        piece = pieces.find_piece(list_pieces, row_up, column_rignt)
                        if self.color != piece.color:
                            self.available_moves.append([row_up, column_rignt])

        if row - 1 >= 0 and column + 1 < constants.column + 1:  # ajoute les cases de la diagonal S.E. du fou tant qu'aucune autre piece n'est trouvée
            for row_down in range(row - 1, constants.row):
                for column_rignt in range(column + 1, constants.column):
                    if row_down == column_rignt:
                        piece = pieces.find_piece(list_pieces, row_down, column_rignt)
                        if self.color != piece.color:
                            self.available_moves.append([row_down, column_rignt])

        if row - 1 >= 0 and column - 1 >= 0:  # ajoute les cases de la diagonal S.O. du fou tant qu'aucune autre piece n'est trouvée
            for row_down in range(row - 1, constants.row):
                for column_rignt in range(column - 1, constants.column):
                    if row_down == column_rignt:
                        piece = pieces.find_piece(list_pieces, row_down, column_rignt)
                        if self.color != piece.color:
                            self.available_moves.append([row_down, column_rignt])

        if row + 1 < constants.row + 1 and column - 1 >= 0:  # ajoute les cases de la diagonal S.O. du fou tant qu'aucune autre piece n'est trouvée
            for row_down in range(row - 1, constants.row):
                for column_rignt in range(column - 1, constants.column):
                    if row_down == column_rignt:
                        piece = pieces.find_piece(list_pieces, row_down, column_rignt)
                        if self.color != piece.color:
                            self.available_moves.append([row_down, column_rignt])

        return self.available_moves