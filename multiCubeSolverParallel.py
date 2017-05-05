# Missouri State University
# CSC 338 Semester Project
import random
import sys
import multiprocessing as mp
import Queue
from dependencies.solutions import beginner3Layer
from dependencies.cube import Cube
import csv

que = mp.Queue()
    
def scramble_and_solve(num_cubes,que):
        print "called"
	cube = Cube(None, None, None)
	num_shuffles = int(1000*random.random())
	move_keys = ["U", "D", "L", "R", "F", "B", "U'", "D'", "L'", "R'", "F'", "B'"]
        for i in range(num_shuffles):
                cube.state.rotate(cube.state.rotationInfo(random.choice(move_keys)))
	solution = cube.getSolution()
	solution_moves = []
	for step in reversed(solution):
		solution_moves.append(step[0])
	que.put([cube.state,solution_moves])

def main(num_cubes, num_processes):
	cubes_per_process = num_cubes // num_processes
	extras = num_cubes % num_processes
	
	processes = []
	for i in range(num_processes):
		process_num_cubes = cubes_per_process
		if extras > 0:
			process_num_cubes += 1
			extras -= 1
		p = mp.Process(target = scramble_and_solve, args = [process_num_cubes, que])
		processes.append(p)
		p.start()
	for p in processes:
		p.join()
		
	scramble_list = []
	solution_list = []
        solution_file = open("solutions.txt", 'w')
        scramble_file = open("scrambles.txt",'w')

	while not que.empty():
                pair = que.get()
                solution_file.write(str(pair[1]))
                scramble_file.write(str(pair[0]))
        solution_file.close()
        scramble_file.close()

if __name__ == "__main__":
	num_cubes = int(sys.argv[1])
	num_processes = int(sys.argv[2])
	main(num_cubes, num_processes)
