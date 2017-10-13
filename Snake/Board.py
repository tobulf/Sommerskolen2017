from TypeClass import*
from random import randint



class Board(object):
    def __init__(self, Size = 5):
        self.chumpos = randint(1,4),randint(1,4)
        self.board = [None]*Size
        for Element in range(Size):
            self.board[Element] = [Tile.Free]*Size



    def CheckPos(self, x, y):
        if  self.board[y][x] == Tile.Chum:
            self.chumpos = randint(1, 4), randint(1, 4)
        return self.board[y][x]

    def SetPos(self,x, y, Tile):
        self.board[y][x] = Tile

