from color import PlayerColor

class Piece:
    WHITE_PAWN = 'P'
    BLACK_PAWN = 'p'
    
    def __init__(self, color: PlayerColor) -> int:
        self.color = color
    
    def __str__(self) -> str:
        return self.WHITE_PAWN if self.color == PlayerColor.WHITE else self.BLACK_PAWN
