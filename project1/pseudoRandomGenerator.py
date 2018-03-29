import random
import sys

def generate():
	file = open("input.txt","w") 
	n = int(sys.argv[1])
	
	for i in range(n):
		x = random.randint(0,9)
		file.write(str(x))

	file.close()

generate()