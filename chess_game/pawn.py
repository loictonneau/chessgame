import chess_game.game
from chess_game import pieces, constants


class Pawn(pieces.Piece):

    def __init__(self, piece_type, color, position):
        super().__init__(piece_type, color, position)
        self.first_move = True

    def get_available_moves(self, list_pieces):  # creer une liste avec tout les coups possibles du pion
        self.clear_available_moves()
        row = self.position[0]
        column = self.position[1]

        if self.color == "white":# si le pion est blanc il avance en retranchant 1 au ligne

            if row - 1 >= 0:  # avance d'une case si elle est vide
                piece = pieces.find_piece(list_pieces, row - 1, column)
                if piece.type is None:
                    self.available_moves.append([row - 1, column])

                    if self.first_move:  # avance de deux case si c'est son premier coup et que cette case est vide
                        piece = pieces.find_piece(list_pieces, row - 2, column)
                        if piece.type is None:
                            self.available_moves.append([row - 2, column])

                if column - 1 >= 0:  # mange une piece adverse en diagonal ( version gauche )
                    piece = pieces.find_piece(list_pieces, row - 1, column - 1)
                    if piece.type is not None:
                        if self.color is not piece.color:
                            self.available_moves.append([row - 1, column - 1])

                if column + 1 < constants.column:  # mange une piece adverse en diagonal ( version droite )
                    piece = pieces.find_piece(list_pieces, row - 1, column + 1)
                    if piece.type is not None:
                        if self.color is not piece.color:
                            self.available_moves.append([row - 1, column + 1])

        if self.color == "black":  # si le pion est noir il avance en ajoutant 1 au ligne

            if row + 1 < constants.row:  # avance d'une case si elle est vide
                piece = pieces.find_piece(list_pieces, row + 1, column)
                if piece.type is None:
                    self.available_moves.append([row + 1, column])

                    if self.first_move:  # avance de deux case si c'est son premier coup et que cette case est vide
                        piece = pieces.find_piece(list_pieces, row + 2, column)
                        if piece.type is None:
                            self.available_moves.append([row + 2, column])

                if column - 1 >= 0:  # mange une piece adverse en diagonal ( version gauche )
                    piece = pieces.find_piece(list_pieces, row + 1, column - 1)
                    if piece.type is not None:
                        if self.color is not piece.color:
                            self.available_moves.append([row + 1, column - 1])

                if column + 1 < constants.column:  # mange une piece adverse en diagonal ( version droite )
                    piece = pieces.find_piece(list_pieces, row + 1, column + 1)
                    if piece.type is not None:
                        if self.color is not piece.color:
                            self.available_moves.append([row + 1, column + 1])

        return self.available_moves
