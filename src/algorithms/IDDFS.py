from copy import copy


def iddfs(game, max_iteration=30):
    iteration = 0
    counter = 0     # number of nodes visited
    while iteration <= max_iteration:
        queue = [game]      # games that needs to be processed
        while queue:
            m = queue.pop()     # pick last inorder to go on each branch in the tree
            # print(m, end="\n")
            if m.check_win():       # if won return game
                print("iddfs")
                print(counter)
                print(m.history)
                return m
            if len(m.history) == iteration:
                # print(len(m.history),iteration)
                continue
            options = []        # all the numbers that can be picked the current game
            for i in range(1, 9):
                if m.check_move(i):
                    options.append(i)
            for number in options:      # for each possible move
                if len(m.history) == 0 or number != m.history[-1]:      # not repeating last step
                    new_game = copy(m)
                    new_game.move(number)
                    queue.append(new_game)
            counter += 1
            del m
        iteration += 1
    print("FAILED")
