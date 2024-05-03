import sys, random
class Puzzle:
    # vals
    board = None            # board is array[3][3]
    free_space = (0, 0)     # free space is the free spot (0) in input
    history = []            # moving tiles in history of game

    def __init__(self, board_string):
        if len(board_string) != 17:
            return
        board = board_string.split(' ')
        self.set_board([[int(board[i * 3 + j]) for j in range(3)] for i in range(3)])

    def __copy__(self):
        ret = Puzzle('')
        ret.set_board([[(self.board[i][j]) for j in range(3)] for i in range(3)])
        ret.history = self.history.copy()
        return ret

    def __str__(self):
        ret = '-' * 5 + '\n'
        for i in range(3):
            # ret += '-' * 7 + '\n|'
            ret += '|'
            for j in range(3):
                # ret += (str(self.board[i][j]) if self.board[i][j] != 0 else ' ') + '|'
                ret += (str(self.board[i][j]) if self.board[i][j] != 0 else ' ')
            ret += "|\n"
        ret += '-' * 5
        return ret

    # set 'board' and 'free_spaces' vals
    def set_board(self, board):
        self.board = board
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    self.free_space = (i, j)

    # get position of number (1-8) on the board
    def get_position(self, number):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == number:
                    return [i, j]

    # commit move
    def move(self, number):
        if not 1 <= number <= 8:
            return
        position = self.get_position(number)
        if self.check_move(number):
            self.board[position[0]][position[1]] = 0
            self.board[self.free_space[0]][self.free_space[1]] = number
            self.free_space = position
            self.history.append(number)
            return True
        else:
            return False

    # check if move is legal
    def check_move(self, number):
        i, j = self.get_position(number)
        return (self.free_space[0] == i + 1 and self.free_space[1] == j) or \
               (self.free_space[0] == i - 1 and self.free_space[1] == j) or \
               (self.free_space[0] == i and self.free_space[1] == j + 1) or \
               (self.free_space[0] == i and self.free_space[1] == j - 1)

    # check if board is winning position
    def check_win(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != (3 * i + j) % 9:
                    return False
        return True

if __name__=="__main__":
    if len(sys.argv) == 10:
        game = Puzzle(' '.join(sys.argv[1:]))
    else:
        board = list(range(9))
        random.shuffle(board)
        game = Puzzle(' '.join(map(str, board)))

    while True:
        print(game)
        game.move(int(input("-->")))
        if game.check_win():
            print("you won!")
            break