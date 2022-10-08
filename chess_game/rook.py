from chess_game import pieces, constants


class Rook(pieces.Piece):

    def __init__(self, piece_type, color, position):
        super().__init__(piece_type, color, position)

    def get_available_moves(self, list_pieces):  # creer une liste avec tout les coups possibles de la tours
        self.clear_available_moves()
        row = self.position[0]
        column = self.position[1]

        if row < constants.row - 1:  # ajoute les cases au dessous de la tours tant qu'aucune autre piece n'est trouvée,
            for row_up in range(row + 1, constants.row):
                piece = pieces.find_piece(list_pieces, row_up, column)
                if piece.type is None:
                    self.available_moves.append([row_up, column])
                elif self.color is not piece.color:  # ajoute la case si une piece adverse est trouvée puis arrete la recherche sinon arrete directement la recherche
                    self.available_moves.append([row_up, column])
                    break
                elif self.color is piece.color :
                    break


        if row > 0 :  # ajoute les cases au dessus de la tours tant qu'aucune autre piece n'est trouvée
            for row_down in range(row - 1, -1, -1):
                piece = pieces.find_piece(list_pieces, row_down, column)
                if piece.type is None:
                    self.available_moves.append([row_down, column])
                elif self.color is not piece.color:# ajoute la case si une piece adverse est trouvée puis arrete la recherche sinon arrete directement la recherche
                    self.available_moves.append([row_down, column])
                    break
                elif self.color is piece.color:
                    break

        if column < constants.column - 1:  # ajoute les cases a droite de la tours tant qu'aucune autre piece n'est trouvée
            for column_right in range(column + 1, constants.column):
                piece = pieces.find_piece(list_pieces, row, column_right)
                print (piece.position)
                if piece.type is None:
                    self.available_moves.append([row, column_right])
                elif self.color is not piece.color:  # ajoute la case si une piece adverse est trouvée puis arrete la recherche sinon arrete directement la recherche
                    self.available_moves.append([row, column_right])
                    break
                elif self.color is piece.color:
                    break

        if column > 0:  # ajoute les cases a gauche de la tours tant qu'aucune autre piece n'est trouvée,
            for column_left in range(column - 1, -1, -1):
                piece = pieces.find_piece(list_pieces, row, column_left)
                if piece.type is None:
                    self.available_moves.append([row, column_left])
                elif self.color is not piece.color:  # ajoute la case si une piece adverse est trouvée puis arrete la recherche sinon arrete directement la recherche
                    self.available_moves.append([row, column_left])
                    break
                elif self.color is piece.color:
                    break


        return self.available_moves

