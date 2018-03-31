import sys
import math
import decimal
from utils import fibonacciNumbers, getBit, primeNumbers

context = decimal.Context(prec=1001)
decimal.setcontext(context)

def getSecretNum(msg, n, x):
	answer = 0
	for i in range(n):
		num = ord(msg[fibonacciNumbers[i]])
		answer |= getBit(num, x) << i
		num = ord(msg[ len(msg) - 1 - fibonacciNumbers[i] ])
		answer |= getBit(num, x) << (n + i)
	
	return answer
		
assert getSecretNum("aaox@r@@w@@@@w@@r@xoaa",6,0) == 2535
assert getSecretNum("aaox@r@@w@@@@w@@r@xoaa",6,1) == 3380
assert getSecretNum("aaox@r@@w@@@@w@@r@xoaa",6,2) == 2340
assert getSecretNum("aaox@r@@w@@@@w@@r@xoaa",6,3) == 780

def getInitialPos(msg):
	return getSecretNum(msg, 7, 0)

def getMsgSize(msg):
	return getSecretNum(msg, 5, 1)

def getKey(msg):
	return primeNumbers[getSecretNum(msg, 5, 2)]

def getInitilPosKey(msg):
	return getSecretNum(msg, 10, 3)

def getParams(msg): 
	return [getInitialPos(msg), getMsgSize(msg), getKey(msg), getInitilPosKey(msg)]

def generateFinalKey(key, initialPosKey, keySize):
	key = decimal.Decimal(key)
	key = str(key.sqrt()).split('.')[1]
	return key[initialPosKey:(initialPosKey+keySize)]

assert generateFinalKey(1,2,2) == "42"
assert generateFinalKey(0,0,5) == "77245"

def getEncriptedMsg(msg, initialPos, msgSize):
	return msg[initialPos:(initialPos+msgSize)]

assert getEncriptedMsg("q393asasdcnjanaaussafasufdicksianoasasnfjanjas", 25, 9) == "dicksiano"

def decode(msg):
	[initialPos, msgSize, key, initilPosKey] = getParams(msg)
	key = generateFinalKey(key, initilPosKey,msgSize)
	encriptedMsg = getEncriptedMsg(msg, initialPos, msgSize)

	return decode(encriptedMsg, key)

def decode(encriptedMsg, key):
	decriptedMsg = ''
	for c, i in zip(encriptedMsg, key):
		decriptedMsg += chr( (ord(c) - int(i))%256 )
	
	return decriptedMsg

assert decode("cbh", "205") == "abc"

	



