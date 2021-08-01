class Player:
    def __init__(self, name):
        if not name.strip().isalnum():
            raise ValueError('Name must only contain letters or numbers only')
        self.name = name
    
    def get_move_input(self, msg = 'Your input: '):
        return input(msg)
