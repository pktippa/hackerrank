# Most of the code is taken from 
# https://github.com/pk-ai/challenges/blob/master/8-puzzle/a_star.py
from heapq import heappush, heappop
goal_state = []
goal_state_matrix = []
given_grid_size = 0
class Node:
    def __init__(self, state, depth, step, parent, score=0):
        self.state = state
        self.depth = depth
        self.step = step
        self.parent = parent
        self.score = score

    def __lt__(self, other):
        return self.score < other.score

def getMatrix(state):
    global given_grid_size
    for i in range(0, len(state), given_grid_size):
        yield state[i:i + given_grid_size]

def getMatrixPos(states_matrix, num):
    global given_grid_size
    for i in range(0,given_grid_size):
        for j in range(0,given_grid_size):
            if states_matrix[i][j] == num:
                return (i,j)

def getPathtoGoal(node):
    path_to_goal = []
    while node.step:
        path_to_goal.insert(0, node.step)
        node = node.parent
    return len(path_to_goal), path_to_goal

def getSteps(node_state):
    global given_grid_size
    node_state_matrix = list(getMatrix(node_state))
    pos = getMatrixPos(node_state_matrix, "0")
    # Can move UP
    if not pos[0] - 1 < 0:
        yield ("UP", (pos, (pos[0] - 1, pos[1])))
    # Can move DOWN
    if not pos[0] + 1 >= given_grid_size:
        yield ("DOWN", (pos, (pos[0] + 1, pos[1])))
    # Can move LEFT
    if not pos[1] - 1 < 0:
        yield ("LEFT", (pos, (pos[0], pos[1] - 1)))
    # Can move RIGHT
    if not pos[1] + 1 >= given_grid_size:
        yield ("RIGHT", (pos, (pos[0], pos[1] + 1)))

def getCombinedList(node_in_matrix):
    returnList = []
    for el in node_in_matrix:
        returnList.extend(el)
    return returnList

def getScore(given_state_matrix):
    sum = 0
    global goal_state
    nums = goal_state[1:]
    for num in nums:
        (i,j) = getMatrixPos(given_state_matrix, num)
        (k,l) = getMatrixPos(goal_state_matrix, num)
        # Manhattan distance for grid/matrix
        sum += abs(i-k) + abs(j-l)
    return sum

def a_star(grid_size, initial_state, given_goal_state):
    nodes_list = []
    states_list = set()
    global goal_state 
    global goal_state_matrix
    global given_grid_size
    goal_state = given_goal_state
    given_grid_size = grid_size
    goal_state_matrix = list(getMatrix(goal_state))
    first_node = Node(initial_state, 0, None, None, 0)
    heappush(nodes_list, (0, first_node))
    states_list.add("".join(initial_state))
    path_to_goal = []
    while True:
        if not nodes_list:
            return len(path_to_goal), path_to_goal
        else:
            node = heappop(nodes_list)[1]
            if node.state == goal_state:
                return getPathtoGoal(node)
            else:
                steps = list(getSteps(node.state))
                for step in steps:
                    new_state = node.state[:]
                    new_state_matrix = list(getMatrix(new_state))
                    (i,j) = step[1][0]
                    (k,l) = step[1][1]
                    new_state_matrix[i][j], new_state_matrix[k][l] = new_state_matrix[k][l], new_state_matrix[i][j]
                    new_state_form = getCombinedList(new_state_matrix)
                    new_state_str = "".join(new_state_form)
                    if new_state_str not in states_list:
                        score = getScore(new_state_matrix) + node.depth + 1
                        new_node = Node(new_state_form, node.depth + 1, step[0], node, score)
                        heappush(nodes_list, (score, new_node))
                        states_list.add(new_state_str)


if __name__ == '__main__':
    grid_size = int(input())
    goal_grid = [str(i) for i in range(grid_size**2)]
    given_grid = []
    for _ in range(grid_size**2):
        given_grid.append(input().strip())
    num_of_moves, goal_path = a_star(grid_size, given_grid, goal_grid)
    print(num_of_moves)
    for step in goal_path:
        print(step)