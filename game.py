class Game:

    def __init__(self):
        self.players = []
        # Id number of active player (0 through total number of players (max 6))
        self.activePlayerIndex = None
        self.tileBag = None
        self.grid = None

    def end_turn(self):
        self.activePlayerIndex = (self.activePlayerIndex + 1) % len(self.players)

