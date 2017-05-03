# Missouri State University
# CSC 338 Semester Project


#NOTE: beginner3Layer tries to write to solutionsLog.txt
#       We'll have to deal with that in parallellizing. (forgive my spelling)

from dependencies.solutions import beginner3Layer
from dependencies.cube import Cube


def main():
    cube = Cube(None, None, None)

# TODO: Figure out the format/object to pass to setConfig.
#       setConfig converts colors to the internal state the solver expects.
#       If we can figure out the input, we can move forward with random and
#       custom inputs.
    cube.setConfig(None)
    print cube
    print cube.getSolution()


if __name__ == "__main__":
    main()
