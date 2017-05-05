# Missouri State University
# CSC 338 Semester Project


#NOTE: beginner3Layer tries to write to solutionsLog.txt
#       We'll have to deal with that in parallellizing. (forgive my spelling)
import random

from dependencies.solutions import beginner3Layer
from dependencies.cube import Cube


def shuffle_cube(cube):
    num_shuffles = int(1000*random.random())
    move_keys = ["U", "D", "L", "R", "F", "B", "U'", "D'", "L'", "R'", "F'", "B'"]
    for i in range(num_shuffles):
        cube.state.rotate(cube.state.rotationInfo(random.choice(move_keys)))
    return cube


def main():
    cube = Cube(None, None, None)
    cube = shuffle_cube(cube)
    print cube.state
    solution = cube.getSolution()
    for step in reversed(solution):
        print step[0],
    


if __name__ == "__main__":
    main()
