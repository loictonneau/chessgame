from chess_game import pieces, utils, constants


class Rook(pieces.Piece):

    def __init__(self, piece_type: str, color: str, position: list):
        super().__init__(piece_type, color, position)
        self.first_move = True

    def get_available_moves(self, list_pieces: list) -> tuple:
        """
        cree un tuple contenant :
            une liste des coordonnée de tous les coups possibles de la tour \n
            coup_possible[coordonné[ligne,colonne]] \n
            une liste des coordonnée de tous les coups possible de la tour ordonnée par direction \n
            coups_possibles[direction[coordonnée[ligne,colonne]]]
        """

        self.clear_available_moves()
        row = self.position[0]
        column = self.position[1]

        # ajoute les cases au dessous de la tours jusqu'a ce qu'une autre piece sois trouvée

        if row + 1 < constants.row:
            available_moves_by_direction = []
            for row_down in range(row + 1, constants.row):

                piece = utils.find_piece(list_pieces, row_down, column)
                if piece.type is None:

                    self.available_moves.append([row_down, column])
                    available_moves_by_direction.append([row_down, column])

                elif self.color is not piece.color:

                    self.available_moves.append([row_down, column])
                    available_moves_by_direction.append([row_down, column])
                    break

                elif self.color is piece.color:

                    break

            self.available_moves_by_direction.append(available_moves_by_direction)

        # ajoute les cases au dessus de la tours jusqu'a ce qu'une autre piece sois trouvée

        if row - 1 >= 0:

            available_moves_by_direction = []
            for row_up in range(row - 1, -1, -1):

                piece = utils.find_piece(list_pieces, row_up, column)

                if piece.type is None:

                    self.available_moves.append([row_up, column])
                    available_moves_by_direction.append([row_up, column])

                elif self.color is not piece.color:

                    self.available_moves.append([row_up, column])
                    available_moves_by_direction.append([row_up, column])
                    break

                elif self.color is piece.color:

                    break

            self.available_moves_by_direction.append(available_moves_by_direction)

        # ajoute les cases a droite de la tours jusqu'a ce qu'une autre piece sois trouvée

        if column + 1 < constants.column:

            available_moves_by_direction = []
            for column_right in range(column + 1, constants.column):
                piece = utils.find_piece(list_pieces, row, column_right)
                if piece.type is None:

                    self.available_moves.append([row, column_right])
                    available_moves_by_direction.append([row, column_right])

                elif self.color is not piece.color:

                    self.available_moves.append([row, column_right])
                    available_moves_by_direction.append([row, column_right])
                    break

                elif self.color is piece.color:

                    break

            self.available_moves_by_direction.append(available_moves_by_direction)

        # ajoute les cases a gauche de la tours jusqu'a ce qu'une autre piece sois trouvée

        if column - 1 >= 0:

            available_moves_by_direction = []
            for column_left in range(column - 1, -1, -1):

                piece = utils.find_piece(list_pieces, row, column_left)
                if piece.type is None:

                    self.available_moves.append([row, column_left])
                    available_moves_by_direction.append([row, column_left])

                elif self.color is not piece.color:

                    self.available_moves.append([row, column_left])
                    available_moves_by_direction.append([row, column_left])
                    break

                elif self.color is piece.color:

                    break

            self.available_moves_by_direction.append(available_moves_by_direction)

        return self.available_moves, self.available_moves_by_direction
