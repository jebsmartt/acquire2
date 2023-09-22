import random
from players import Player
from game import Game

def start_game():
    #instantiate a game
    game = Game()
    
    # Append player objects to list in game instance
    for p in Player.current_players:
        game.players.append(p)

    # Set initial active player id (0 through total number of players (max 6))
    game.active_player_index = random.randint(0, len(Player.current_players)-1)

    return game