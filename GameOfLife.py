from collections import defaultdict
from input import aliveCells

class GameOfLife:
    def __init__(self, aliveCells, rows, columns):
        self.aliveCells = set(aliveCells)
        self.rows = rows
        self.columns = columns

    def tick(self):
        aliveNeighbors = defaultdict(int)
        dirs = [(-1,-1), (-1,0), (-1,1), (1, -1), (1,0), (1,1), (0,1), (0,-1)]
        for r, c in self.aliveCells:
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                aliveNeighbors[(nr, nc)] += 1

        nextAliveCells = set()
        for r, c in aliveNeighbors:
            numAliveNeighbors = aliveNeighbors[(r, c)]
            if numAliveNeighbors == 3 or ((r, c) in aliveCells and numAliveNeighbors == 2):
                nextAliveCells.add((r, c))
        self.aliveCells = nextAliveCells

    def __str__(self):
        output = ""
        for c in range(self.columns):
            for r in range(self.rows):
                output += 'O|' if (r, c) in self.aliveCells else ' |'
            output += "\n"
        return output
    
    def printAliveCells(self):
        print(self.aliveCells)

game = GameOfLife(aliveCells, 8, 8)
print(game)
game.printAliveCells()
game.tick()
print(game)
game.printAliveCells()