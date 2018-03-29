import sys
import math
import decimal

context = decimal.Context(prec=1001)
decimal.setcontext(context)

def encode():
	plainMsg = sys.argv[1] # Read plain message
	key = decimal.Decimal(int(sys.argv[2])) # Read key
	key = str(key.sqrt()).split('.')[1] #
	encriptedMsg = ' '
	
	for c in plainMsg:
		if(c == ' '):
			encriptedMsg += ' '
		else:


encode()