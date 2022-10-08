from chess_game import pieces, constants


class Pawn(pieces.Piece):

    def __init__(self, piece_type, color, position):
        super().__init__(piece_type, color, position)
        self.first_move = True

    def get_available_move(self, list_pieces):  # creer une liste avec tout les coups possibles du pion
        self.clear_available_move()

        row = self.position[0]
        column = self.position[1]

        if self.color == "white":
            # si le pion est blanc il avance en retranchant 1 au ligne
            if row - 1 >= 0:
                piece = pieces.Piece.find_piece(self,list_pieces,row - 1,column)
                if piece.type is None:  # verifie que la case est vide
                    self.available_move.append([row - 1, column])  # ajoute la case aux coups possibles

                    # si le pion n'a jamais bouger il peut egalement avancer de deux cases d'un coup
                    if self.first_move:
                        piece = pieces.Piece.find_piece(self, list_pieces, row - 2, column)
                        if piece.type is None:  # verifie que la case est vide
                            self.available_move.append([row - 2, column])  # ajoute la case aux coups possibles

                if column-1 >= 0:# le pion peut manger en diagonal ( version gauche )
                    piece = pieces.Piece.find_piece(self,list_pieces,row - 1,column -1)
                    if piece.type is not None:  # verifie qu'il y a une piece sur la case
                        if self.color is not piece.color:  # verifie qu'il s'agis d'une piece adverse
                            self.available_move.append([row - 1, column - 1])  # ajoute la case aux coups possibles

                if column+1 >= 0: # le pion peut manger en diagonal ( version droite )
                    piece = pieces.Piece.find_piece(self,list_pieces,row - 1,column + 1)
                    if piece.position == [row - 1, column + 1]:  # trouve la case corespondante
                        if piece.type is not None:  # verifie qu'il y a une piece sur la case
                            if self.color is not piece.color:  # verifie qu'il s'agis d'une piece adverse
                                self.available_move.append([row - 1, column + 1])# ajoute la case aux coups possibles

        if self.color == "black":
            # si le pion est noir il avance en ajoutant 1 au ligne
            if row + 1 >= 0:
                piece = pieces.Piece.find_piece(self, list_pieces, row + 1, column)
                if piece.type is None:  # verifie que la case est vide
                    self.available_move.append([row + 1, column])  # ajoute la case aux coups possibles

                    # si le pion n'a jamais bouger il peut egalement avancer de deux cases d'un coup
                    if self.first_move:
                        piece = pieces.Piece.find_piece(self, list_pieces, row + 2, column)
                        if piece.type is None:  # verifie que la case est vide
                            self.available_move.append([row + 2, column])  # ajoute la case aux coups possibles

                if column - 1 >= 0:  # le pion peut manger en diagonal ( version gauche )
                    piece = pieces.Piece.find_piece(self, list_pieces, row + 1, column - 1)
                    if piece.type is not None:  # verifie qu'il y a une piece sur la case
                        if self.color is not piece.color:  # verifie qu'il s'agis d'une piece adverse
                            self.available_move.append([row + 1, column - 1])  # ajoute la case aux coups possibles

                if column + 1 >= 0:  # le pion peut manger en diagonal ( version droite )
                    piece = pieces.Piece.find_piece(self, list_pieces, row + 1, column + 1)
                    if piece.position == [row - 1, column + 1]:  # trouve la case corespondante
                        if piece.type is not None:  # verifie qu'il y a une piece sur la case
                            if self.color is not piece.color:  # verifie qu'il s'agis d'une piece adverse
                                self.available_move.append([row + 1, column + 1])  # ajoute la case aux coups possibles

        return self.available_move
