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
                find = False
                for pieces1 in list_pieces:
                    if not find:
                        for piece1 in pieces1:
                            if piece1.position == [row - 1, column]:  # trouve la case corespondante
                                if piece1.type is None:  # verifie que la case est vide
                                    self.available_move.append([row - 1, column])  # ajoute la case aux coups possibles

                                    # si le pion n'a jamais bouger il peut egalement avancer de deux cases d'un coup
                                    if self.first_move:
                                        find = False
                                        for pieces2 in list_pieces:
                                            if not find:
                                                for piece2 in pieces2:
                                                    # trouve la case corespondante
                                                    if piece2.position == [row - 2, column]:
                                                        if piece2.type is None:  # verifie que la case est vide
                                                            # ajoute la case aux coups possibles
                                                            self.available_move.append([row - 2, column])
                                                            find = True
                                                            break
                                            elif find:
                                                break
                                    find = True
                                    break
                    elif find:
                        break

                # le pion peut manger en diagonal ( version gauche )
                if column-1 >= 0:
                    find = False
                    for pieces3 in list_pieces:
                        if not find:
                            for piece3 in pieces3:
                                if piece3.position == [row - 1, column - 1]:  # trouve la case corespondante
                                    if piece3.type is not None:  # verifie qu'il y a une piece sur la case
                                        if piece3.color is not self.color:  # verifie qu'il s'agis d'une piece adverse
                                            # ajoute la case aux coups possibles
                                            self.available_move.append([row - 1, column - 1])
                                            find = True
                                            break

                # le pion peut manger en diagonal ( version droite )
                if column+1 >= 0:
                    find = False
                    for pieces4 in list_pieces:
                        if not find:
                            for piece4 in pieces4:
                                if piece4.position == [row - 1, column + 1]:  # trouve la case corespondante
                                    if piece4.type is not None:  # verifie qu'il y a une piece sur la case
                                        if piece4.color is not self.color:  # verifie qu'il s'agis d'une piece adverse
                                            # ajoute la case aux coups possibles
                                            self.available_move.append([row - 1, column + 1])
                                            find = True
                                            break
        if self.color == "black":

            # si le pion est noir il avance en additionnant 1 au ligne
            if row + 1 < constants.row:
                find = False
                for pieces5 in list_pieces:
                    if not find:
                        for piece5 in pieces5:
                            if piece5.position == [row + 1, column]:  # trouve la case corespondante
                                if piece5.type is None:  # verifie que la case est vide
                                    self.available_move.append([row + 1, column])  # ajoute la case aux coups possibles

                                    # si le pion n'a jamais bouger il peut egalement avancer de deux case d'un coup
                                    if self.first_move:
                                        find = False
                                        for pieces6 in list_pieces:
                                            if not find:
                                                for piece6 in pieces6:
                                                    # trouve la case corespondante
                                                    if piece6.position == [row + 2, column]:
                                                        if piece6.type is None:  # verifie que la case est vide
                                                            # ajoute la case aux coups possibles
                                                            self.available_move.append([row + 2, column])
                                                            find = True
                                                            break
                                            elif find:
                                                break
                                    find = True
                                    break
                    elif find:
                        break

                # le pion peut manger en diagonal ( version gauche )
                if column-1 >= 0:
                    find = False
                    for pieces7 in list_pieces:
                        if not find:
                            for piece7 in pieces7:
                                if piece7.position == [row + 1, column - 1]:  # trouve la case corespondante
                                    if piece7.type is not None:  # verifie qu'il y a une piece sur la case
                                        if piece7.color is not self.color:  # verifie qu'il s'agis d'une piece adverse
                                            # ajoute la case aux coups possibles
                                            self.available_move.append([row + 1, column - 1])
                                            find = True
                                            break

                # le pion peut manger en diagonal ( version droite )
                if column+1 >= 0:
                    find = False
                    for pieces8 in list_pieces:
                        if not find:
                            for piece in pieces8:
                                if piece.position == [row + 1, column + 1]:  # trouve la case corespondante
                                    if piece.type is not None:  # verifie qu'il y a une piece sur la case
                                        if piece.color is not self.color:  # verifie qu'il s'agis d'une piece adverse
                                            # ajoute la case aux coups possibles
                                            self.available_move.append([row + 1, column + 1])
                                            find = True
                                            break

        return self.available_move
