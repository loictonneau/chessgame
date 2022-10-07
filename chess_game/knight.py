from . import pieces


class Knight(pieces.Piece):

    def __init__(self, piece_type, color, position):
        super().__init__(piece_type, color, position)
