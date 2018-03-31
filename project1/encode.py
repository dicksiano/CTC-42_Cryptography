import sys
import math
import decimal
import random

context = decimal.Context(prec=1001001)
decimal.setcontext(context)

def generateFirstTrash(initialPos):
	trash = ''

	for x in range(initialPos - 1):
		trash += chr(random.randint(0,255))

	return trash

assert len(generateFirstTrash(5)) == 4

def generateSecondTrash(initialPos, msgSize):
	trash = ''

	for x in range(initialPos + msgSize, 10000):
		trash += chr(random.randint(0,255))

	return trash

assert len(generateSecondTrash(8990, 1000)) == 10

def encode(plainText, key):
	encriptedMsg = ''
	for c, i in zip(plainText, key):
		encriptedMsg += chr( (ord(c) + int(i))%256 )

	return encriptedMsg

assert encode("abc", "205") == "cbh"
