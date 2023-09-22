class Game:

    def __init__(self):
        self.players = []
        # Id number of active player (0 through total number of players (max 6))
        self.active_player_index = None

    def end_turn(self):
        self.active_player_index = (self.active_player_index + 1) % len(self.players)