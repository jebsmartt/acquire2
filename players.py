class Player:
    player_ids = [0,1,2,3,4,5]
    current_players = []

    def __init__(self, type):

        self.type = type    # Expect 0 for PC or 1 for human player
        self.id = Player.player_ids.pop(0)
        Player.current_players.append(self)
        self.tile_rack = []

    def print_player(self):
        print(f'PlayerId = {self.id}, PlayerType = {self.type}')

    def draw_tile(self,tile_bag):
        selectedTile = tile_bag.contents.pop(0)
        return selectedTile


    def show_tile_rack(self):
        pp_tile_rack = []
        for t in self.tile_rack:
            pp_tile_rack.append(t.name)
        print(f"Tile_rack: {pp_tile_rack}")