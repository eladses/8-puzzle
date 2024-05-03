import sys

from src.Puzzle import Puzzle

from src.algorithms.BFS import bfs
from src.algorithms.IDDFS import iddfs
from src.algorithms.GBFS import gbfs
from src.algorithms.A_star import a_star

IDDFS_ITERATIONS = 12

def main():
    if len(sys.argv) != 10:
        print("[INPUT PROBLEM]: Usage - python Tiles.py" + " _" * 9)
        return

    game = Puzzle(' '.join(sys.argv[1:]))  # create game

    # try different algorithms
    print(game)
    bfs(game)
    print()
    iddfs(game, IDDFS_ITERATIONS)
    print()
    gbfs(game)
    print()
    a_star(game)



if __name__ == "__main__":
    main()
