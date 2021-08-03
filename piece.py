class Piece:
    WHITE_PAWN = 'P'
    BLACK_PAWN = 'p'
    
    def __init__(self, color: str) -> int:
        if color not in ('w', 'b'):
            raise ValueError('Color must only be `w` or `b` ')
        self.color = color
    
    def __str__(self) -> str:
        return self.WHITE_PAWN if self.color == 'w' else self.BLACK_PAWN
