#!/usr/bin/python

# Head ends here
from heapq import heappush, heappop
class Node:
    def __init__(self, pos, step, score=0):
        self.pos = pos
        self.step = step
        self.score = score

    def __lt__(self, other):
        return self.score < other.score

def next_move(posr, posc, board):
    if(board[posr][posc] == 'd'):
        print("CLEAN")
    else:
        nearest_dirt_pos = getNearestDirtPos(posr, posc, board)
        bot_pos = (posr, posc)
        nodes_list = []
        moves = getAvailableMoves(bot_pos, board)
        for move in moves:
            score = abs(move[1][0] - nearest_dirt_pos[0]) + abs(move[1][1] - nearest_dirt_pos[1])
            new_node = Node(move[1], move[0], score)
            heappush(nodes_list, (score, new_node))
        print(heappop(nodes_list)[1].step)

def getNearestDirtPos(posr, posc, board):
    distance = 20
    nearest_dirt_place_pos = None
    for i in range(5):
        for j in range(5):
            if board[i][j] == 'd':
                dist_to_dirt_place = abs(i - posr) + abs(j - posc)
                if distance > dist_to_dirt_place:
                    distance = dist_to_dirt_place
                    nearest_dirt_place_pos = (i, j)
    return nearest_dirt_place_pos

# Moves as Up, Down, Left, Right - UDLR
def getAvailableMoves(pos, board):
    # Can move UP
    try:
        x = board[pos[0] - 1][pos[1]]
        yield ("UP", (pos[0] - 1, pos[1]))
    except:
        pass
    # Can move Down
    try:
        x = board[pos[0] + 1][pos[1]]
        yield ("DOWN", (pos[0] + 1, pos[1]))
    except:
        pass
    # Can move Left
    try:
        x = board[pos[0]][pos[1] - 1]
        yield ("LEFT", (pos[0], pos[1] - 1))
    except:
        pass
    # Can move Right
    try:
        x = board[pos[0]][pos[1] + 1]
        yield ("RIGHT", (pos[0], pos[1] + 1))
    except:
        pass


# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
