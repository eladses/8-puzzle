import math
from copy import copy
from .functions.functions import predicted_cost

# find most promising node in queue
def most_promising_node(queue):
    min_index = 0
    min_cost = math.inf
    for i in range(len(queue)):
        current_cost = predicted_cost(queue[i].board)
        if current_cost < min_cost:
            min_index = i
            min_cost = current_cost

    return min_index


def gbfs(game):
    counter = 0  # number of nodes visited
    visited = [game.board]  # board that have been visited or correctly in queue
    queue = [game]  # games that needs to be processed

    while queue:
        m = queue.pop(most_promising_node(queue))  # pick first most promising node
        if m.check_win():  # if won return game
            print("gbfs")
            print(counter)
            print(m.history)
            return m
        options = []  # all the numbers that can be picked the current game
        for i in range(1, 9):
            if m.check_move(i):
                options.append(i)
        for number in options:  # for each possible move
            new_game = copy(m)  # create a copy of game
            new_game.move(number)  # then try the move

            if new_game.board not in visited:  # if not been here
                queue.append(new_game)  # add it to the queue
                visited.append(new_game.board)  # and add it the visited
            else:
                del new_game
        counter += 1
        del m
