import os

str1  = "1\n"

bytesStr1 = bytes(str1, 'ascii')

configDataIniFile = open(os.getcwd() + "/1.ini", "wb+")
configDataIniFile.write(bytesStr1)
configDataIniFile.close()

print(bytesStr1)