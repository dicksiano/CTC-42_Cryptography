from decode import decoder
from encode import encoder
f1 = open("file1.txt", 'wb')
f2 = open("file2.txt", 'wb')
str1 = encoder('godofwarpauplatinapaunotoba')
str2 = encoder('godofwarpalplatinapaunotoba')

f1.write(str1.encode('utf8'))
f2.write(str2.encode('utf8'))
f1.close()
f2.close()