class Tile:

    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.name = f'{row}{column}'

class TileBag:
    rows = ['A','B','C','D','E','F','G','H','I']
    columns = [1,2,3,4,5,6,7,8,9,10]

    def __init__(self):
        self.contents = []

    def fill_bag(self):
        for r in TileBag.rows:
            for c in TileBag.columns:
                new_tile = Tile(r,c)
                self.contents.append(new_tile)

class Space:

    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.name = f'{row}{column}'

class Grid:
    rows = ['A','B','C','D','E','F','G','H','I']
    columns = [1,2,3,4,5,6,7,8,9,10]

    def __init__(self):
        self.spaces = []

    def set_grid(self):
        for r in Grid.rows:
            for c in Grid.columns:
                space = Space(r,c)
                self.spaces.append(space)

    def print_grid(self):
        pp_grid = []
        for s in self.spaces:    
            pp_grid.append(s.name)
        print(pp_grid)