class Piece:
    def __init__(self, piece_type, color, position):
        self.type = piece_type
        self.color = color
        self.position = position

    def __str__(self):
        if self.color is None:
            return "n"

        elif self.color == "black":

            if self.type == "pawn":
                return "p"
            elif self.type == "rook":
                return "t"
            elif self.type == "knight":
                return "c"
            elif self.type == "bishop":
                return "f"
            elif self.type == "queen":
                return "d"
            elif self.type == "king":
                return "r"

        elif self.color == "white":

            if self.type == "pawn":
                return "P"
            elif self.type == "rook":
                return "T"
            elif self.type == "knight":
                return "C"
            elif self.type == "bishop":
                return "F"
            elif self.type == "queen":
                return "D"
            elif self.type == "king":
                return "R"
