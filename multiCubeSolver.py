# Missouri State University
# CSC 338 Semester Project


#NOTE: beginner3Layer tries to write to solutionsLog.txt
#       We'll have to deal with that in parallellizing. (forgive my spelling)

from dependencies.solutions import beginner3Layer
from dependencies.cube import CubeState
def main():
    state = CubeState()
    print state
    solution = beginner3Layer(state)
    print solution


if __name__ == "__main__":
    main()
