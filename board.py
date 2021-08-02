from string import ascii_uppercase
from typing import List

class Board:
    IDENTIFIER = ascii_uppercase
    NONE_STR = '.'
    SPACER = ' '
    MAXIMUM_ROW_AND_LENGTH = 26

    def __init__(self, row: int, column: int):
        MAX = self.MAXIMUM_ROW_AND_LENGTH
        error_str = f"{{}} must be greater than 0 and less than or equal to {MAX}"
        
        if not 0 <= row <= MAX:
            raise ValueError(error_str.format('Row'))
        self.row = row
        
        if not 0 <= row <= MAX:
            raise ValueError(error_str.format('Column'))
        self.column = column
        
        self.board = [[None for _ in range(column)] for _ in range(row)]
    
    def __getitem__(self, index: int) -> List:
        return self.board[index]
    
    def __str__(self):
        str_ = []
        SPACER = self.SPACER
        NONE_STR = self.NONE_STR
        
        for index, row in enumerate(self.board, 1):
            row = [str(item) if item is not None else NONE_STR for item in row]
            row.append(str(index))
            str_.append(SPACER.join(row))
        str_.insert(0, SPACER.join(self.IDENTIFIER[:index]))
        
        return '\n'.join(str_)
