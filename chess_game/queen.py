from chess_game import pieces, bishop, rook


class Queen(pieces.Piece):

    def __init__(self, piece_type: str, color: str, position: list[int, int]):
        super().__init__(piece_type, color, position)

    def get_available_moves(self, list_pieces: list[pieces.Piece]) -> tuple[list[list[int, int]],
                                                                            list[list[list[int, int]]]]:
        """
        cree un tuple contenant :
            une liste des coordonnée de tous les coups possibles du reine \n
            coup_possible[coordonné[ligne,colonne]] \n
            une liste des coordonnée de tous les coups possible du reine ordonnée par direction \n
            coups_possibles[direction[coordonnée[ligne,colonne]]]
        """

        # la reine peut bouger a la fois comme un fou et comme une tour
        bishop_move = bishop.Bishop.get_available_moves(self, list_pieces)
        rook_move = rook.Rook.get_available_moves(self, list_pieces)

        self.available_moves = sorted(bishop_move[0] + rook_move[0])
        self.available_moves_by_direction = sorted(bishop_move[1] + rook_move[1])

        return self.available_moves, self.available_moves_by_direction
