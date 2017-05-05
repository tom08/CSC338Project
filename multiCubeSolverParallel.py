# Missouri State University
# CSC 338 Semester Project

# To Run: python multiCubeSolverParallel.py <num_cubes> <num_processes>
import random
import sys
import multiprocessing as mp
from dependencies.solutions import beginner3Layer
from dependencies.cube import Cube
import time
import os

que = mp.Queue()

    
def scramble_and_solve(num_cubes, que, process_num):
	with open("solutions" + process_num + ".txt", 'w') as solution_file:
		with open("scramble" + process_num + ".txt", 'w') as scramble_file:
			for i in range(num_cubes):
				cube = Cube(None, None, None)
				num_shuffles = int(1000*random.random())
				move_keys = ["U", "D", "L", "R", "F", "B", "U'", "D'", "L'", "R'", "F'", "B'"]
				for j in range(num_shuffles):
					cube.state.rotate(cube.state.rotationInfo(random.choice(move_keys)))
				solution = cube.getSolution()
				solution_moves = []
				for step in reversed(solution):
					solution_moves.append(step[0])
				solution_file.write(str(solution_moves))
				scramble_file.write(str(cube.state))
	que.put(("solutions" + process_num + ".txt", "scramble" + process_num + ".txt"))

def main(num_cubes, num_processes):
	cubes_per_process = num_cubes // num_processes
	extras = num_cubes % num_processes
	processes = []
	for i in range(num_processes):
		process_num_cubes = cubes_per_process
		if extras > 0:
			process_num_cubes += 1
			extras -= 1
		p = mp.Process(target = scramble_and_solve, args = [process_num_cubes, que, str(i)])
		processes.append(p)
		p.start()
	for p in processes:
		p.join()
	
	with open('solutions.txt', 'w') as solution_outfile:
		with open('scrambles.txt', 'w') as scramble_outfile:
			while not que.empty():
				pair = que.get()
				with open(pair[0],'r') as infile:
					for line in infile:
						solution_outfile.write(line)
				with open(pair[1],'r') as infile:
					for line in infile:
						scramble_outfile.write(line)
				os.remove(pair[0])
				os.remove(pair[1])
					

start = time.time()
if __name__ == "__main__":
	num_cubes = int(sys.argv[1])
	num_processes = int(sys.argv[2])
	main(num_cubes, num_processes)
	print "Total time: ", time.time()-start
