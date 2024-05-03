import math

def predicted_cost(board):
    return manhattan_distance(board)
    # return corners_distances(board)

###############################################################
#                     heuristic functions                     #
###############################################################

def manhattan_distance(board):
    cost = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != 0:
                cost += math.fabs(math.floor(board[i][j] / 3) - i)
                cost += math.fabs(board[i][j] % 3 - j)
    return cost

def corners_distances(board):
    cost = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 2:
                cost += i + (2 - j)
            elif board[i][j] == 6:
                cost += (2 - i) + j
            elif board[i][j] == 8:
                cost += (2 - i) + (2 - j)
    return cost/2
    