import sys
import math
import decimal

context = decimal.Context(prec=1001)
decimal.setcontext(context)

def encode():
	plainMsg = sys.argv[1] # Read plain message
	key = decimal.Decimal(int(sys.argv[2])) # Read key
	key = str(key.sqrt()).split('.')[1] # Get 1000 digits of the square root
	
	file = open("input.txt","w")

	for c, i in zip(plainMsg, key):
		file.write(chr( (ord(c) - int(i))%256 ))

	file.close()

encode()