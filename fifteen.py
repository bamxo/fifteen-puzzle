# author: Landon Nguyen
# date: March 17, 2023
# file: fifteen.py a Python file that the game fifteen puzzle
# input: users input numbers 1-15 to move tiles around the board to get them in order
# output: prints current state of the board

import numpy as np
from random import choice
from graph import Graph

class Fifteen:
    
    def __init__(self, size = 4):
        self.size = size
        self.tiles = np.array([i for i in range(1,size**2)] + [0])
        self.adj = [[j for j in [i - 1, i + 1, i - size, i + size] if j >= 0 and j < size ** 2 and abs(j % size - i % size) + abs(j // size - i // size) == 1] for i in range(size ** 2)]
        self.layout = Graph()
        for i in range(size**2):
            vertex = self.layout.addVertex(i)
            row, col = i // size, i % size
            if row > 0:
                self.layout.addEdge(i, i - size)
            if row < size - 1:
                self.layout.addEdge(i, i + size)
            if col > 0:
                self.layout.addEdge(i, i - 1)
            if col < size - 1:
                self.layout.addEdge(i, i + 1)

    def update(self, move):
        if self.is_valid_move(move):
            for i in range(len(self.tiles)):
                if self.tiles[i] == move:
                    self.tiles[i] = -1
                if self.tiles[i] == 0:
                    self.tiles[i] = move
            for i in range(len(self.tiles)):
                if self.tiles[i] == -1:
                    self.tiles[i] = 0
        
    def transpose(self, i, j):
        self.tiles[i], self.tiles[j] = self.tiles[j], self.tiles[i]
    
    def shuffle(self, steps=100):
        index = np.where(self.tiles == 0)[0][0]
        for i in range(steps):
            move_index = choice (self.adj[index])
            self.tiles[index],self.tiles[move_index] = self.tiles[move_index],self.tiles[index]
            index = move_index
        
        
    def is_valid_move(self, move):
        ans = False
        values = [i for i in range(1,17)]
        board = {k:v for (k,v) in zip(values,self.tiles)}
        placement = [k for k, v in board.items() if v == move][0]
        if placement == 1:
            if board[placement + 1] == 0 or board[placement + 4] == 0:
                ans = True
        elif placement in [2,3]:
            if board[placement - 1] == 0 or board[placement + 1] == 0 or board[placement + 4] == 0:
                ans = True
        elif placement == 4:
            if board[placement - 1] == 0 or board[placement + 4] == 0:
                ans = True
        elif placement in [5,9]:
            if board[placement - 4] == 0 or board[placement + 1] == 0 or board[placement + 4] == 0:
                ans = True
        elif placement in [8,12]:
            if board[placement - 4] == 0 or board[placement - 1] == 0 or board[placement + 4] == 0:
                ans = True
        elif placement == 13:
            if board[placement - 4] == 0 or board[placement + 1] == 0:
                ans = True
        elif placement in [14,15]:
            if board[placement - 1] == 0 or board[placement - 4] == 0 or board[placement + 1] == 0:
                ans = True
        elif placement == 16:
            if board[placement - 4] == 0 or board[placement - 1] == 0:
                ans = True
        else:
            if board[placement - 1] == 0 or board[placement + 1] == 0 or board[placement - 4] == 0 or board[placement + 4] == 0:
                ans = True
        return ans

    def is_solved(self):
        arr = np.array([i for i in range(1,4**2)] + [0])
        for i in range(len(self.tiles)):
            if self.tiles[i] != arr[i]:
                return False
        return True

    def draw(self):
        for i in range(self.size):
            print("+---" * self.size + "+")
            for j in range(self.size):
                if self.tiles[i * self.size + j] == 0:
                    print("|   ", end="")
                else:
                    print("|{:2d} ".format(self.tiles[i * self.size + j]), end="")
            print("|")
        print("+---" * self.size + "+")
        
    def __str__(self):
        s = ''
        tracker = 0
        for i in self.tiles:
            if i == 0:
                s += '   '
            else:
                if tracker == 4:
                    tracker = 0
                    s += '\n'
                if i > 9:
                    s += f'{i} '
                else:
                    s += f' {i} '
                tracker += 1
        return s + '\n'

if __name__ == '__main__':
    
    game = Fifteen()
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_valid_move(15) == True
    assert game.is_valid_move(12) == True
    assert game.is_valid_move(14) == False
    assert game.is_valid_move(1) == False
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14    15 \n'
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == True
    game.shuffle()
    assert str(game) != ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == False
    
    
    '''You should be able to play the game if you uncomment the code below'''
    '''
    game = Fifteen()
    game.shuffle()
    game.draw()
    while True:
        move = input('Enter your move or q to quit: ')
        if move == 'q':
            break
        elif not move.isdigit():
            continue
        game.update(int(move))
        game.draw()
        if game.is_solved():
            break
    print('Game over!')
    '''
    
    
        
