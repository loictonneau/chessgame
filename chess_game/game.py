from chess_game import constants,pieces,pawn,rook,knight,bishop,queen,king






class Game:

    def __init__(self):
        piece_list = []

        for row in range (constants.row):
            rows = []
            for column in range (constants.column):

                if row == 0:
                    if column == 0 or column == 7:
                        rows.append(rook.Rook("rook", "white", [row, column]))
                    elif column == 1 or column == 6:
                        rows.append(knight.Knight("knight","white",[row,column]))
                    elif column == 2 or column == 5:
                        rows.append(bishop.Bishop("bishop","white",[row,column]))
                    elif column == 3:
                        rows.append(queen.Queen("knight","white",[row,column]))
                    elif column == 4 :
                        rows.append(king.King("king","white", [row,column]))

                if row == 1 :
                    rows.append(pawn.Pawn("pawn","white", [row,column]))

                if row >= 2 and row <= 5:
                    rows.append(pieces.Piece(None,None,[row,column]))

                if row == 6 :
                    rows.append(pawn.Pawn("pawn","black", [row,column]))

                if row == 7:
                    if column == 0 or column == 7:
                        rows.append(rook.Rook("rook", "black", [row, column]))
                    elif column == 1 or column == 6:
                        rows.append(knight.Knight("knight", "black", [row, column]))
                    elif column == 2 or column == 5:
                        rows.append(bishop.Bishop("bishop", "black", [row, column]))
                    elif column == 3:
                        rows.append(queen.Queen("knight", "black", [row, column]))
                    elif column == 4:
                        rows.append(king.King("king", "black", [row, column]))

            piece_list.append(rows)

    def print_board(self):
        pass


