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
    def __init__(self, x, y, live=False):
        """
        :param x: int, x coordinate
        :param y: int, y coordinate
        :param live: bool, is the cell alive?
        """
        self.x = x
        self.y = y
        self.live = live

    def display(self):
        return '*' if self.live else '.'

class GameOfLife():
    def __init__(self, cells, steps):
        """
        :param cells: list, of cell coordinates
        :param steps: int, number of steps the game will complete
        """
        self.cells = cells
        self.steps = steps-1  # inc tick during play
        self.tick = 0

        self.min_x = self.min_y = 100
        self.max_x = self.max_y = -100

        self.set_board()
        # initial (tick 0 display)
        self.display()

    def set_board(self):
        for c in self.cells:
            self.max_x = max(self.max_x, c.x)
            self.max_y = max(self.max_y, c.y)
            self.min_x = min(self.min_x, c.x)
            self.min_y = min(self.min_y, c.y)

        self.board = [
            [Cell(x, y) for x in range(self.min_x, self.max_x+1)]
                for y in range(self.min_y, self.max_y+1)]

        for cell in self.cells:
            self.get_point(cell.x, cell.y).live = True

    def get_point(self, x, y):
        return self.board[y-self.min_y][x-self.min_x]

    def display(self):
        """
        Display board with:
        X from left -> right
        Y from bottom -> top
        0th row included
        """
        print(f"\nTick #{self.tick}:")
        for i in range(len(self.board)-1, -1, -1):
            print([c.display() for c in self.board[i]])

    def set_cell(self, cell):
        neighboring_coords = [
            (cell.x-1, cell.y-1),
            (cell.x-1, cell.y),
            (cell.x-1, cell.y+1),
            (cell.x, cell.y-1),
            (cell.x, cell.y+1),
            (cell.x+1, cell.y-1),
            (cell.x+1, cell.y),
            (cell.x+1, cell.y+1),
        ]
        # count living neighbors
        live_count = 0
        for nx, ny in neighboring_coords:
            if self.min_x <= nx <= self.max_x and self.min_y <= ny <= self.max_y:
                if self.get_point(nx, ny).live:
                    live_count += 1
        # set live
        if cell.live:
            if live_count < 2 or live_count > 3:
                cell.live = False
                self.cells = [c for c in self.cells if c != cell]
        else:
            if live_count == 3:
                cell.live = True
                self.cells.append(cell)

    def play(self):
        while self.tick <= self.steps:
            new_min_x = new_min_y = 100
            new_max_x = new_max_y = -100
            for y in range(len(self.board)):
                for x in range(len(self.board[y])):
                    self.set_cell(self.board[y][x])
                    new_max_x = max(new_max_x, x)
                    new_max_y = max(new_max_y, y)
                    new_min_x = min(new_min_x, x)
                    new_min_y = min(new_min_y, y)

            # finish out
            self.tick += 1
            self.display()

            # redefine board
            self.min_x = new_min_x
            self.min_y = new_min_y
            self.max_x = new_max_x
            self.max_y = new_max_y
            self.set_board()


game = GameOfLife(
    cells=[Cell(2, 3), Cell(1, 3), Cell(1, 5), Cell(4, 3), Cell(4, 2),
           Cell(4, 1), Cell(1, 1), Cell(0, 0), Cell(0, 5), Cell(5, 1),
           Cell(3, 3), Cell(1, 4), Cell(3, 5), Cell(5, 3), Cell(2, 2),
           Cell(4, 5), Cell(4, 4), Cell(0, 3), Cell(0, 2), Cell(3, 1)],
    steps=9)
game.play()

