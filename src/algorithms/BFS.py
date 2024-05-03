from copy import copy


def bfs(game):
    counter = 0                 # number of nodes visited
    visited = [game.board]      # board that been visited or correctly in queue
    queue = [game]              # games that needs to be processed
    while queue:
        m = queue.pop(0)        # pick first inorder to go on each layer in the tree
        # print(m, end="\n")    # print the board of the node in process
        if m.check_win():       # if won return game
            print("bfs")
            print(counter)
            print(m.history)
            return m

        options = []            # all the numbers that can be picked the current game
        for i in range(1, 9):
            if m.check_move(i):
                options.append(i)
        for number in options:      # for each possible move
            new_game = copy(m)      # create a copy of game
            new_game.move(number)   # then try the move

            if new_game.board not in visited:   # if not been here
                queue.append(new_game)          # add it to the queue
                visited.append(new_game.board)  # and add it the visited
            else:
                del new_game
        counter += 1
        del m
