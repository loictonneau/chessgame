
def find_piece(list_pieces, row, column):
    try :
        for pieces in list_pieces:
            for piece in pieces:
                if piece.position == [row, column]:
                    raise StopIteration
    except StopIteration:
        return piece


class Piece:
    def __init__(self, piece_type, color, position):
        self.type = piece_type
        self.color = color
        self.position = position
        self.available_moves = []

    def clear_available_moves(self):
        if len(self.available_moves) > 0:
            self.available_moves = []


