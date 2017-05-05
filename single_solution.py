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
	moves = ["B'",  "R",  "L'",  "U", "U",  "L",  "R'",  "D'",  "F",  "R'",  "B",  "L'",  "D'",
			  "L", "L",  "B",  "D", "D",  "U", "U", "F","F",  "U",  "D",  "L",  "B'",  "R",  "L","L",  "B",  "L"]
	for move in moves:
		print move,
	print 
	print
	for i in range(len(moves)):
		cube.state.rotate(cube.state.rotationInfo(moves[i]))
	solution = cube.getSolution()
	for step in solution:
		print step[0],

def main():
	scramble_and_solve()
	
main()