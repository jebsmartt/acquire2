import random
from game import Game
from players import Player
from tiles import Tile,TileBag

def start_game():
    #instantiate a game
    game = Game()

    # Append player objects to list in game instance
    for p in Player.current_players:
        game.players.append(p)

    # Set initial active player id (0 through total number of players (max 6))
    game.activePlayerIndex = random.randint(0, len(Player.current_players)-1)

    #instantiate tile bag
    tileBag = TileBag()
    tileBag.fill_bag()
    # TODO add random.shuffle(tileBag.contents)
    game.tileBag = tileBag
    
    active_player = game.players[game.activePlayerIndex]

    # draw initial tile set and add objects to player tileBag
    for p in game.players:
        print(f'\nDrawing for Player ID {p.id}')
        while len(p.tile_rack) < 6:
            p.tile_rack.append(p.draw_tile(game.tileBag))
        print(f'Here is the len of the tile rack: {len(p.tile_rack)}')    
        p.show_tile_rack()
    

    return game