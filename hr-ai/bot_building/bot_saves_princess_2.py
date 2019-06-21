#!/usr/bin/python3
# Most part of code is copied from bot_saves_princess.py
# Logic is to use Priority Queue with A* search algorithm
from heapq import heappush, heappop
princess_pos = None
given_grid = None
bot_pos = None
class Node:
    def __init__(self, pos, step, score=0):
        self.pos = pos
        self.step = step
        self.score = score

    def __lt__(self, other):
        return self.score < other.score
# Moves as Up, Down, Left, Right - UDLR
def getAvailableMoves(pos):
    global given_grid
    # Can move UP
    try:
        given_grid[pos[0] - 1][pos[1]] = "-"
        yield ("UP", (pos[0] - 1, pos[1]))
    except:
        pass
    # Can move Down
    try:
        given_grid[pos[0] + 1][pos[1]] = "-"
        yield ("DOWN", (pos[0] + 1, pos[1]))
    except:
        pass
    # Can move Left
    try:
        given_grid[pos[0]][pos[1] - 1] = "-"
        yield ("LEFT", (pos[0], pos[1] - 1))
    except:
        pass
    # Can move Right
    try:
        given_grid[pos[0]][pos[1] + 1] = "-"
        yield ("RIGHT", (pos[0], pos[1] + 1))
    except:
        pass

def getBotPrincessPos(n, grid):
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'p':
                princess_pos = (i, j)
                break
    return princess_pos

def getScore(new_bot_pos):
    global princess_pos
    return abs(princess_pos[0] - new_bot_pos[0]) + abs(princess_pos[1] - new_bot_pos[1])

def nextMove(n,r,c,grid):
    global princess_pos
    global bot_pos
    global given_grid
    given_grid = grid
    bot_pos = (r, c)
    princess_pos = getBotPrincessPos(n, grid)
    nodes_list = []
    states_list = set()
    states_list.add(str(bot_pos))
    moves = getAvailableMoves(bot_pos)
    for move in moves:
        if str(move[1]) not in states_list:
            score = getScore(move[1])
            new_node = Node(move[1], move[0], score)
            heappush(nodes_list, (score, new_node))
            states_list.add(str(move[1]))
    node = heappop(nodes_list)[1]
    return node.step
n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(list(input().strip()))

print(nextMove(n,r,c,grid))
