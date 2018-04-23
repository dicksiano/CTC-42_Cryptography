import sys
import math
import decimal
import utils
from utils import fibonacciNumbers, getBit, primeNumbers

def decimalPrecision(precision):
	context = decimal.Context(precision)
	decimal.setcontext(context)

def getSecretNum(msg, n, x):
	answer = 0
	for i in range(n):
		num = ord(msg[fibonacciNumbers[i]])
		answer |= getBit(num, x) << i
		num = ord(msg[ len(msg) -1 - fibonacciNumbers[i] ])
		answer |= getBit(num, x) << (n + i)
	
	return answer
		
assert getSecretNum("aaox@r@@w@@@@w@@r@xoaa",6,0) == 2535
assert getSecretNum("aaox@r@@w@@@@w@@r@xoaa",6,1) == 3380
assert getSecretNum("aaox@r@@w@@@@w@@r@xoaa",6,2) == 2340
assert getSecretNum("aaox@r@@w@@@@w@@r@xoaa",6,3) == 780

def getInitialPos(msg):
	return getSecretNum(msg, int(utils.NUM_BITS_INITIAL_POS/2), 0)

def getMsgSize(msg):
	return getSecretNum(msg, int(utils.NUM_BITS_MSG_SIZE/2), 1)

def getKey(msg):
	return primeNumbers[getSecretNum(msg, int(utils.NUM_BITS_KEY/2), 2)]

def getInitilPosKey(msg):
	return getSecretNum(msg, int(utils.NUM_BITS_KEY_INITIAL_POS/2), 3)

def getParams(msg): 
	return [getInitialPos(msg), getMsgSize(msg), getKey(msg), getInitilPosKey(msg)]

def generateFinalKey(key, initialPosKey, keySize):
	decimalPrecision(initialPosKey+keySize+2)
	key = decimal.Decimal(key)
	key = str(key.sqrt()).split('.')[1]
	return key[initialPosKey:(initialPosKey+keySize)]

assert generateFinalKey(primeNumbers[1],2,2) == "42" 
assert generateFinalKey(primeNumbers[0],0,5) == "77245"

def getEncriptedMsg(msg, initialPos, msgSize):
	return msg[initialPos:(initialPos+msgSize)]

assert getEncriptedMsg("q393asasdcnjanaaussafasufdicksianoasasnfjanjas", 25, 9) == "dicksiano"

def decode(encriptedMsg, key):
	decriptedMsg = ''
	for c, i in zip(encriptedMsg, key):
		pos = key.index(i)
		str = key[pos:pos+3]
		decriptedMsg += chr( (ord(c) - int(str))%256 )
	
	return decriptedMsg

assert decode(".gh", "205") == "abc"

def decoder(msg):
	[initialPos, msgSize, key, initilPosKey] = getParams(msg)
	key = generateFinalKey(key, initilPosKey, msgSize)
	encriptedMsg = getEncriptedMsg(msg, initialPos, msgSize)

	return decode(encriptedMsg, key)

# Test considering the key sum one number by one number, now changed to sum by 3 and 3 numbers
# fT = [209,88,192,120,98,16,145,16,32,64]
# lT = [128,64,32,16,32,64,128,64,32,16]
# le = chr(fT[0])+chr(fT[1])+chr(fT[2])+chr(fT[3])+"a"+chr(fT[4])+\
# 	 "aa"+chr(fT[5])+"aaaa"+chr(fT[6])+"aaaaaaa"+chr(fT[7])+"aaaaaaaaaaaa"+\
# 	 chr(fT[8])+"aaaaaaaaaaaaaaaaaaaa"+chr(fT[9])
# ld = chr(fT[9])+"aaaaaaaaaaaaaaaaaaaa"+chr(fT[8])+"aaaaaaaaaaaa"+\
# 	 chr(lT[7])+"aaaaaaa"+chr(lT[6])+"aaaa"+chr(lT[5])+"aa"+\
# 	 chr(lT[4])+"a"+chr(lT[3])+chr(lT[2])+chr(lT[1])+chr(lT[0])
# la = "444444444"
# lde = "asjhladjbkcalfjdblas"
# em = "eshs~y}gkrfxtjhe"
# encr = le+la+em+lde+ld

# assert decoder(le+la+em+lde+ld) == "encryptedmessage"

	



