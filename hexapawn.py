from board import Board
from player import Player
from piece import Piece

class Hexapawn:
    def __init__(self, board, players:tuple):
        if not isinstance(board, Board):
            raise TypeError('board must be a Board object')
        if board.row != 3 or board.column != 3:
            raise Error('board must only have 3 rows and 3 columns')
        
        for index, player in enumerate(players):
            if index > 1:
                raise Error('Players must only be 2')
            if isinstance(player, Player):
                continue
            raise TypeError(f"player at index {index} must be a Player object")
        
        self.players = tuple(players)
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
    
    def change_white_turn(self, value = None):
        is_white_turn = self.is_white_turn
        
        if value is None:
            self.is_white_turn = False if is_white_turn else True
            return
        
        if not isinstance(value, bool):
             raise TypeError(f"{value} must be type bool.")
        
        self.is_white_turn = value
    
    def is_stalemate(self):
        board = self.board
        get_piece_moves_at = self.get_piece_moves_at
        
        for y in range(board.row):
            for x in range(board.column):
                try:
                    if get_piece_moves_at(y, x) != []:
                        return True
                except TypeError:
                    continue
        return False
    
    def is_player_at_end(self, player):
        if not isinstance(player, Player):
            raise TypeError('player must be an instance of Player')
        
        board = self.board
        player_index = self.players.index(player) * -1
        color = self.colors[player_index]
        
        for x in board[player_index]: 
            try:
                if x.color != color:
                    continue
                return True
            except AttributeError:
                continue
        return False
    
    def is_win(self):
        return is_stalemate() or is_current_player_at_end(self.current_player)
    
    def move_piece(self, current, future):
        y, x = current
        piece = self.board[y][x]
        
        if piece is None:
            raise Error('There is no Piece in location')
        
        if piece.color != self.current_color:
            raise Error('The piece is not yours')
        
        if future not in self.get_piece_moves_at(y, x):
            raise Error('Cannot move to given future')
        
        self.board[y][x] = None
        self.board[future[0]][future[-1]] = piece
    
    def get_piece_direction_by_color(self, piece):
        if not isinstance(piece, Piece):
            raise TypeError('piece must an instance of Piece')
        
        return -1 if piece.color == 'w' else 1
    
    def get_piece_moves_at(self, row, column):
        board = self.board
        piece = board[row][column]
        
        if not isinstance(piece, Piece):
            raise TypeError(f"Object at {row, column} must be an instance of piece.")
        
        direction = get_piece_direction(piece)
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
                    moves.apppend((new_y, new_x))
                continue
            except IndexError:
                continue 
            except AttributeError:
                continue
        return moves
    
    def start_game_in_terminal(self):
        self.is_on_going = True
        
        while self.is_in_progress:
            print(str(self.board))
            before, after = self.current_player.get_move_input().split("|")
            
            self.move_piece(before.split(","), after.split(","))
            
            if self.is_win():
                print(self.current_player.name + 'won!')
                return
            
            self.change_white_turn()
    
    def set_up_board_with(self, piece):
        board = self.board
        
        for y, color in ((0, 'b'), (-1, 'w')):
            for x in range(board.column):
                board[y][x] = piece(color)
