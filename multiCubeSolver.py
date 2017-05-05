# Missouri State University
# CSC 338 Semester Project

import random
import time
import sys
import Queue

from dependencies.solutions import beginner3Layer
from dependencies.cube import Cube

solution_file = open("solutions_serial.txt", 'w')
scramble_file = open("scrambles_serial.txt",'w') 

def scramble_and_solve():
	cube = Cube(None, None, None)
	num_shuffles = int(1000*random.random())
	move_keys = ["U", "D", "L", "R", "F", "B", "U'", "D'", "L'", "R'", "F'", "B'"]
	for i in range(num_shuffles):
		cube.state.rotate(cube.state.rotationInfo(random.choice(move_keys)))
	solution = cube.getSolution()
	solution_moves = []
	for step in reversed(solution):
		solution_moves.append(step[0])
	solution_file.write(str(solution_moves))
	scramble_file.write(str(cube.state))

def main(num_cubes):
	scramble_list = []
	solution_list = []
	for i in range(num_cubes):
	    scramble_and_solve()
	solution_file.close()
	scramble_file.close()

start = time.time()
if __name__ == "__main__":
	num_cubes = int(sys.argv[1])
	main(num_cubes)
	print "Total time: ", time.time()-start