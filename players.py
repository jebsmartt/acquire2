class Player:
    player_ids = [0,1,2,3,4,5]
    current_players = []

    def __init__(self, type):

        self.type = type    # Expect 0 for PC or 1 for human player
        self.id = Player.player_ids.pop(0)
        Player.current_players.append(self)

    def print_player(self):
        print(f'PlayerId = {self.id}, PlayerType = {self.type}')

