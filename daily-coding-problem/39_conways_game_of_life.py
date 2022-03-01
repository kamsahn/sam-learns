"""
Conway's Game of Life takes place on an infinite two-dimensional board of square
cells. Each cell is either dead or alive, and at each tick, the following rules
apply:

Any live cell with less than two live neighbours dies.
Any live cell with two or three live neighbours remains living.
Any live cell with more than three live neighbours dies.
Any dead cell with exactly three live neighbours becomes a live cell.
A cell neighbours another cell if it is horizontally, vertically, or diagonally
adjacent.

Implement Conway's Game of Life. It should be able to be initialized with a
starting list of live cell coordinates and the number of steps it should run
for. Once initialized, it should print out the board state at each step. Since
it's an infinite board, print out only the relevant coordinates, i.e. from the
top-leftmost live cell to bottom-rightmost live cell.

You can represent a live cell with an asterisk (*) and a dead cell with a dot
(.).
"""

class Cell():
    def __init__(self, x, y):
        """
        :param x: int, x coordinate
        :param y: int, y coordinate
        :param live: bool, is the cell alive?
        """
        self.x = x
        self.y = y

class GameOfLife():
    def __init__(self, cells, steps):
        """
        :param cells: list, of cell coordinates
        :param steps: int, number of steps the game will complete
        """
        self.cells = cells
        self.steps = steps-1  # inc tick during play
        self.tick = 0

        # max_x = max_y = -100
        # min_x = min_y = 100
        # for c in cells:
        #     max_x = max(max_x, c.x)
        #     max_y = max(max_y, c.y)
        #     min_x = min(min_x, c.x)
        #     min_y = min(min_y, c.y)

        self.board = [['.' for x in range(10)] for y in range(10)]  # todo use min and max
        for cell in cells:
            self.board[cell.y][cell.x] = '*'


    def display(self):
        """
        Display board with:
        X from left -> right
        Y from bottom -> top
        0th row included
        """
        print(f"\nTick #{self.tick}:")
        for i in range(len(self.board)-1, -1, -1):
            print(self.board[i])

    def set_cell(self, x, y, live):
        neighboring_coords = [
            (x-1, y-1),
            (x-1, y),
            (x-1, y+1),
            (x, y-1),
            (x, y+1),
            (x+1, y-1),
            (x+1, y),
            (x+1, y+1),
        ]
        # count living neighbors
        live_count = 0
        for nx, ny in neighboring_coords:
            if -1 < nx < 10 and -1 < ny < 10:
                if self.board[ny][nx] == '*':
                    live_count += 1

        # set live
        if live:
            if live_count < 2 or live_count > 3:
                self.board[y][x] = '.'

        else:
            if live_count == 3:
                self.board[y][x] = '*'

    def play(self):
        self.display()
        while self.tick <= self.steps:
            for y in range(len(self.board)):
                for x in range(len(self.board[y])):
                    self.set_cell(x, y, self.board[y][x] == '*')

            # finish out
            self.tick += 1
            self.display()


game = GameOfLife(
    cells=[Cell(2, 3), Cell(1, 3), Cell(1, 5), Cell(4, 3), Cell(4, 2),
           Cell(4, 1), Cell(1, 1), Cell(0, 0), Cell(0, 5), Cell(5, 1),
           Cell(3, 3), Cell(1, 4), Cell(3, 5), Cell(5, 3), Cell(2, 2),
           Cell(4, 5), Cell(4, 4), Cell(0, 3), Cell(0, 2), Cell(3, 1)],
    steps=9)
game.play()

