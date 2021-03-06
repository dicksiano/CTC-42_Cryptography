import random
import utils
import decimal 

def decimalPrecision(precision):
	context = decimal.Context(precision)
	decimal.setcontext(context)

def generateTrash(initialPos, msgSize):
	trash1 = ''
	trash2 = ''

	for x in range(initialPos):
		trash1 += chr(random.randint(0,255))
	for x in range(initialPos + msgSize, utils.MESSAGE_SIZE):
		trash2 += chr(random.randint(0,255))

	return [trash1, trash2]

[trashA, trashB] = generateTrash(8990,1000)
assert len(trashA) == 8990
assert len(trashB) == 10

def addInfo(first, second, x, size, position):

	first = list(first)
	second = list(second)

	for i in range(int(size)):
		# change letter in first trash
		num = ord(first[ utils.fibonacciNumbers[i] ]) # current char
		bit = utils.getBit(x, i) # the bit of info x is '0' or '1'
		first[ utils.fibonacciNumbers[i] ] = chr(utils.changeBit(num, bit, position)) # set the 'bit'

		# change letter in second trash
		num = ord(second[ len(second) -1 - utils.fibonacciNumbers[i] ]) # current char
		bit = utils.getBit(x, i + int(size)) # the bit of info x is '0' or '1'
		second[ len(second) -1 - utils.fibonacciNumbers[i] ] = chr(utils.changeBit(num, bit, position)) # set the 'bit'

	return [''.join(first), ''.join(second)]

[a,b] = addInfo("dddd", "xxxx", 0b10011001, 4, 0)
assert a == "edde"
assert b == "yxxy"

def addInfoInitPos(first, second, initialPos):
	return addInfo(first, second, initialPos, utils.NUM_BITS_INITIAL_POS/2, 0)

[a,b] = addInfoInitPos("dddddddddddddd", "xxxxxxxxxxxxxx", 0b11111111111111)
assert a == "eeeededdedddde"
assert b == "yxxxxyxxyxyyyy"
[a,b] = addInfoInitPos("gggggggggggggg", "xxxxxxxxxxxxxx", 0)
assert a == "ffffgfggfggggf"
assert b == "xxxxxxxxxxxxxx"
																
def addInfoMsgSize(first, second, msgSize):
	return addInfo(first, second, msgSize, utils.NUM_BITS_MSG_SIZE/2, 1)

def addInfoKey(first, second, key):
	return addInfo(first, second, key, utils.NUM_BITS_KEY/2, 2)

def addInfoInitPosKey(first, second, initialPosKey):
	return addInfo(first, second, initialPosKey, utils.NUM_BITS_KEY_INITIAL_POS/2, 3)

def addInformationInsideTrash(firstTrash, secondTrash, initialPos, msgSize, key, initialPosKey):
	[firstTrash, secondTrash] = addInfoInitPos(firstTrash, secondTrash, initialPos)
	[firstTrash, secondTrash] = addInfoMsgSize(firstTrash, secondTrash, msgSize)
	[firstTrash, secondTrash] = addInfoKey(firstTrash, secondTrash, key)
	[firstTrash, secondTrash] = addInfoInitPosKey(firstTrash, secondTrash, initialPosKey)
	return [firstTrash, secondTrash]

def generateFinalKey(key, initialPosKey, keySize):
	decimalPrecision(initialPosKey+keySize*3+2)
	key = decimal.Decimal(key)
	key = str(key.sqrt()).split('.')[1]
	# return key[initialPosKey:(initialPosKey+keySize)]
	return key[initialPosKey:(initialPosKey+keySize*3)]

def encode(plainText, key):
	encriptedMsg = ''
	pos = 0
	# for c, i in zip(plainText, key):
	for c in plainText:
		# pos = key.index(i)
		str = key[pos:pos+3]
		encriptedMsg += chr( (ord(c) + int(str))%256 )
		pos += 3

	return encriptedMsg

# assert encode("abc", "205005005") == ".gh"

def innerEncoder(plainText, initialPos, key, initialKeyPos):
	[firstTrash, secondTrash] = generateTrash(initialPos, len(plainText))
	[firstTrash, secondTrash] = addInformationInsideTrash(firstTrash, secondTrash, initialPos, len(plainText), key, initialKeyPos)
	key = generateFinalKey(utils.primeNumbers[key], initialKeyPos, len(plainText))
	encodedText = encode(plainText, key)

	## AQUI RIVA
	f1 = open(plainText + '.txt', 'wb')
	f1.write(encodedText.encode('utf8'))
	return (firstTrash + encodedText + secondTrash)

# str = encoder("encryptedmessage", 65,0,10)

def encoder(plainText):
	initialPos = random.randint(55,10000-55-len(plainText))
	key = random.randint(0,500)
	initialKeyPos = random.randint(0,100000)

	return innerEncoder(plainText, initialPos, key, initialKeyPos)