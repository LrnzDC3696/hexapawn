from typing import Optional

class Player:
    def __init__(self, name: str) -> None:
        if not name.strip().isalnum():
            raise ValueError('Name must only contain letters or numbers only')
        self.name = name
    
    def get_move_input(self, msg: Optional[str] = 'Your input: ') -> str:
        return input(msg)
