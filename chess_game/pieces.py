class Piece:

    def __init__(self, piece_type, color, position: list[int, int]):
        self.type = piece_type
        self.color = color
        self.position = position
        self.available_moves = []
        self.available_moves_by_direction = []

    def clear_available_moves(self):
        """
        s'assure que la listes des coups disponibles
        et la liste des coup disponible triée pas direction sois vide
        si elles ne le sont pas elle les remet a vide
        """

        if len(self.available_moves) > 0:

            self.available_moves = []

        if len(self.available_moves_by_direction) > 0:

            self.available_moves_by_direction = []

    def first_move_done(self):
        """change la possibilité des coups speciaux lié au premier deplacement"""

        if self.type in ("pawn", "rook", "king"):

            self.first_move = False
