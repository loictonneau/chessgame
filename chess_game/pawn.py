from chess_game import pieces


class Pawn(pieces.Piece):

    def __init__(self, piece_type, color, position):
        super().__init__(piece_type, color, position)
        self.first_move = True
