class Piece:
    def __init__(self, piece_type, color, position):
        self.type = piece_type
        self.color = color
        self.position = position
        self.available_move = []

    def clear_available_move(self):
        if len(self.available_move) > 0:
            self.available_move = []
