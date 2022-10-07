from . import pieces


class King(pieces.Piece):

    def __init__(self, piece_type, color, position):
        super().__init__(piece_type, color, position)
