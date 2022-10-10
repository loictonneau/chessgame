from . import pieces, bishop, rook


class Queen(pieces.Piece):

    def __init__(self, piece_type, color, position):
        super().__init__(piece_type, color, position)

    def get_available_moves(self, list_pieces):  # cree une liste avec tous les coups possibles de la reine
        # la reine peut bouger a la fois comme un fou et comme une tour
        bishop_move = bishop.Bishop.get_available_moves(self, list_pieces)
        rook_move = rook.Rook.get_available_moves(self, list_pieces)
        self.available_moves = sorted(bishop_move + rook_move)
        return self.available_moves
