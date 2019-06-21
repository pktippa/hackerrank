#!/usr/bin/python3
from heapq import heappush, heappop
princess_pos = None
given_grid = None
class Node:
    def __init__(self, pos, depth, step, parent, score=0):
        self.pos = pos
        self.depth = depth
        self.step = step
        self.parent = parent
        self.score = score

    def __lt__(self, other):
        return self.score < other.score

def displayPathtoPrincess(n,grid):
    global princess_pos
    global given_grid
    given_grid = grid
    bot_pos, princess_pos = getBotAndPrincessPos(n, grid)
    nodes_list = []
    states_list = set()
    final_node = None
    first_node = Node(bot_pos, 0, None, None, 0)
    heappush(nodes_list, (0, first_node))
    states_list.add(str(bot_pos))
    while True:
        if not nodes_list:
            break
        else:
            node = heappop(nodes_list)[1]
            if node.pos == princess_pos:
                final_node = node
                break
            else:
                moves = getAvailableMoves(node.pos)
                for move in moves:
                    if str(move[1]) not in states_list:
                        score = getScore(move[1]) + node.depth + 1
                        new_node = Node(move[1], node.depth + 1, move[0], node, score)
                        heappush(nodes_list, (score, new_node))
                        states_list.add(str(move[1]))
    if final_node:
        path_to_goal = getPathtoGoal(final_node)
        for step in path_to_goal:
            print(step)

def getPathtoGoal(node):
    path_to_goal = []
    while node.step:
        path_to_goal.insert(0, node.step)
        node = node.parent
    return path_to_goal

def getScore(new_bot_pos):
    global princess_pos
    return abs(princess_pos[0] - new_bot_pos[0]) + abs(princess_pos[1] - new_bot_pos[1])

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

def getBotAndPrincessPos(n, grid):
    bot_pos_found = False
    princes_pos_found = False
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'm':
                bot_pos_found = True
                bot_pos = (i, j)
            elif grid[i][j] == 'p':
                princes_pos_found = True
                princess_pos = (i, j)
            if bot_pos_found and princes_pos_found:
                break
    return bot_pos, princess_pos

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(list(input().strip()))

displayPathtoPrincess(m,grid)
