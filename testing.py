from players import Player
from engine import start_game

# test data
playerA = Player(0)
playerB = Player(0)
playerC = Player(0)
playerD = Player(1)

test_game = start_game()

print(f'\n________')
test_game.grid.print_grid()
# print(test_game.grid.spaces[-1].name)