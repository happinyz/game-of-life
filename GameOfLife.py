from collections import defaultdict
from input import aliveCellsInput

class GameOfLife:
    def __init__(self, aliveCells, rows, columns):
        self.aliveCells = set(aliveCells)
        self.rows = rows
        self.columns = columns

    def tick(self, numTicks = 1):
        for i in range(numTicks):
            aliveNeighbors = defaultdict(int)
            dirs = [(-1,-1), (-1,0), (-1,1), (1, -1), (1,0), (1,1), (0,1), (0,-1)]
            for x, y in self.aliveCells:
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    aliveNeighbors[(nx, ny)] += 1

            nextAliveCells = set()
            for x, y in aliveNeighbors:
                numAliveNeighbors = aliveNeighbors[(x, y)]
                if numAliveNeighbors == 3 or ((x, y) in self.aliveCells and numAliveNeighbors == 2):
                    nextAliveCells.add((x, y))
            self.aliveCells = nextAliveCells

    def __str__(self):
        output = ""
        for y in range(self.columns):
            for x in range(self.rows):
                output += 'O|' if (x, y) in self.aliveCells else ' |'
            output += "\n"
        return output
    
    def printAliveCells(self):
        print(self.aliveCells)
    
game = GameOfLife(aliveCellsInput, 8, 8)
print(game)
game.printAliveCells()

game.tick(10)
print(game)
game.printAliveCells()