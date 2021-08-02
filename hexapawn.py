from typing import Optional, List, Union, Tuple

from board import Board
from player import Player
from piece import Piece

class Hexapawn:
    ROW = 3
    COLUMN = 3
    
    def __init__(self, board: Board, player1: Player, player2: Player):
        if not isinstance(board, Board):
            raise TypeError('board must be a Board object')
        
        if board.row != self.ROW or board.column != self.COLUMN:
            raise Exception('board must only have 3 rows and 3 columns')
        
        for player in (player1, player2):
            if isinstance(player, Player):
                continue
            raise TypeError('player at must be a Player object')
        
        self.players = (player1, player2)
        self.board = board
        self.is_on_going = False
        self.is_white_turn = True
    
    @property
    def current_player_index(self):
        return 0 if self.is_white_turn else -1
    
    @property
    def current_player(self):
        return self.players[self.current_player_index]
    
    @property
    def current_color(self):
        return 'w' if self.is_white_turn else 'b'
    
    @property
    def current_direction(self):
        return -1 if self.is_white_turn else 1
    
    def change_white_turn(self, value: Optional[bool] = None):
        is_white_turn = self.is_white_turn
        
        if value is None:
            self.is_white_turn = False if is_white_turn else True
            return
        
        if not isinstance(value, bool):
             raise TypeError(f"{value} must be type bool.")
        
        self.is_white_turn = value
    
    def is_stalemate(self) -> bool:
        board = self.board
        get_piece_moves_at = self.get_piece_moves_at
        
        for y in range(board.row):
            for x in range(board.column):
                try:
                    if get_piece_moves_at(y, x) != []:
                        return False
                except TypeError:
                    continue
        return True
    
    def is_player_at_end(self, player: Player) -> bool:
        if not isinstance(player, Player):
            raise TypeError('player must be an instance of Player')
        
        board = self.board
        player_index = self.players.index(player) * -1
        color = 'w' if player_index == 0 else 'b'
        
        for x in board[player_index]: 
            try:
                if x.color != color:
                    continue
                return True
            except AttributeError:
                continue
        return False
    
    def is_win(self) -> bool:
        return self.is_stalemate() or self.is_player_at_end(self.current_player)
    
    def move_piece(self, current: Union[List[int], Tuple[int]], future: Union[List[int], Tuple[int]]):
        y, x = current
        piece = self.board[y][x]
        
        if piece is None:
            raise Exception('There is no Piece in location')
        
        if piece.color != self.current_color:
            raise Exception('The piece is not yours')
        
        if tuple(future) not in self.get_piece_moves_at(y, x):
            raise Exception('Cannot move to given future')
        
        self.board[y][x] = None
        self.board[future[0]][future[-1]] = piece
    
    def get_piece_direction_by_color(self, piece: Piece) -> int:
        if not isinstance(piece, Piece):
            raise TypeError('piece must an instance of Piece')
        
        return -1 if piece.color == 'w' else 1
    
    def get_piece_moves_at(self, y: int, x: int) -> List[Tuple[int]]:
        board = self.board
        piece = board[y][x]
        
        if not isinstance(piece, Piece):
            raise TypeError(f"Object at {x, y} must be an instance of piece.")
        
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
    
    def start_game_in_terminal(self):
        self.is_on_going = True
        
        while self.is_on_going:
            print(str(self.board))
            
            before, after = self.current_player.get_move_input().split("|")
            before = [int(x) for x in before.split(",")]
            after = [int(x) for x in after.split(",")]
            
            try:
                self.move_piece(before, after)
            except:
                print(f"Available moves: {self.get_piece_moves_at(*before)}")
                continue
            
            if self.is_win():
                print(self.current_player.name + 'won!')
                return
            
            self.change_white_turn()
    
    def set_up_board_with(self, piece: Piece):
        board = self.board
        
        for y, color in ((0, 'b'), (-1, 'w')):
            for x in range(board.column):
                board[y][x] = piece(color)
