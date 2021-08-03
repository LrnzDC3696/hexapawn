from string import ascii_uppercase
from typing import List

class Board:
    FILE_IDENTIFIER = ascii_uppercase # File as in the column 
    MAXIMUM_ROW_AND_LENGTH = 26
    NONE_STR = '.'
    SPACER = ' '

    def __init__(self, row: int, column: int) -> None:
        MAX = self.MAXIMUM_ROW_AND_LENGTH
        error_str = f"{{}} must be greater than 0 and less than or equal to {MAX}"
        
        if not 0 <= row <= MAX:
            raise ValueError(error_str.format('Row'))
        self.row = row
        
        if not 0 <= column <= MAX:
            raise ValueError(error_str.format('Column'))
        self.column = column
        
        self.board = [[None for _ in range(column)] for _ in range(row)]
    
    def __getitem__(self, index: int) -> List:
        return self.board[index]
    
    def __str__(self) -> str:
        str_ = []
        SPACER = self.SPACER
        NONE_STR = self.NONE_STR
        
        for index, row in enumerate(self.board, 1):
            row = [str(item) if item is not None else NONE_STR for item in row]
            row.append(str(index))
            str_.append(SPACER.join(row))
        str_.insert(0, SPACER.join(self.FILE_IDENTIFIER[:index]))
        
        return '\n'.join(str_)
