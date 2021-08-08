from typing import List, Optional, Tuple, Union

from board import Board
from color import PlayerColor
from piece import Piece
from player import Player

class Hexapawn:
    ROW = 3
    COLUMN = 3
    
    def __init__(self, board: Board, player_white: Player, player_black: Player, is_white_turn: bool = True) -> None:
        if board.row != self.ROW or board.column != self.COLUMN:
            raise Exception('board must only have 3 rows and 3 columns')
        
        self.board = board
        self.player_white = player_white
        self.player_black = player_black
        self._current_player_color = PlayerColor.WHITE if is_white_turn else PlayerColor.BLACK
        
        self.is_on_going = False
    
    @property
    def current_player(self):
        return self.player_white if self._current_player_color == PlayerColor.WHITE else self.player_black
    
    def change_turn(self) -> None:
        self._current_player_color = PlayerColor.WHITE if self._current_player_color == PlayerColor.BLACK else PlayerColor.BLACK
    
    def get_piece_direction_by_color(self, piece: Piece) -> int:
        return -1 if piece.color == PlayerColor.WHITE else 1
    
    def get_piece_moves_at(self, y: int, x: int) -> List[Tuple[int, int]]:
        board = self.board
        piece = board[y][x]
        direction = self.get_piece_direction_by_color(piece)
        moves = []
        new_y = y + direction
        
        try:
            if board[new_y][x] is None:
                moves.append((new_y, x))
        except IndexError:
            return []
        
        for x_ in (1, -1):
            new_x = x + x_
            try:
                if board[new_y][new_x].color != piece.color:
                    moves.append((new_y, new_x))
            except IndexError:
                continue
            except AttributeError:
                continue
            
        return moves
    
    def is_stalemate(self) -> bool:
        board = self.board
        get_piece_moves_at = self.get_piece_moves_at
        
        for y in range(board.row):
            for x in range(board.column):
                try:
                    if get_piece_moves_at(y, x) != []:
                        return False
                except AttributeError:
                    continue
        return True
    
    def is_player_at_end(self, player: Player) -> bool:
        board = self.board
        color = self._current_player_color
        end_index = 0 if color == PlayerColor.WHITE else -1
        
        for x in board[end_index]: 
            try:
                if x.color != color:
                    continue
                return True
            except AttributeError:
                continue
        return False
    
    def is_win(self) -> bool:
        return self.is_stalemate() or self.is_player_at_end(self.current_player)
    
    def move_piece(self, current: Union[List[int], Tuple[int]], future: Union[List[int], Tuple[int]]) -> None:
        y, x = current
        piece = self.board[y][x]
        
        if piece is None:
            raise Exception('There is no Piece in location')
        
        if piece.color != self._current_player_color:
            raise Exception('The piece is not yours')
        
        if tuple(future) not in self.get_piece_moves_at(y, x):
            raise Exception('Cannot move to given future')
        
        self.board[y][x] = None
        self.board[future[0]][future[-1]] = piece
    
    def start_game_in_terminal(self) -> None:
        self.is_on_going = True
        move_piece = self.move_piece
        
        while self.is_on_going:
            print(str(self.board))
            
            # will refactor soon
            before, after = self.current_player.get_move_input().split("|")
            before = [int(x) for x in before.split(",")]
            after = [int(x) for x in after.split(",")]
            
            try:
                move_piece(before, after)
            except:
                print(f"Available moves: {self.get_piece_moves_at(*before)}")
                continue
            
            if self.is_win():
                print(self.current_player.name + 'won!')
                return
            
            self.change_turn()
