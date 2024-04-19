#只限於大寫
def CaesarCipher(str,key,encrypt):
    result = ""

    for i in range(len(str)):
        if(ord(str[i] )== 32):
            result += " "
        else:
            temp = ord(str[i]) - 65
            if(encrypt == "encrypt"):
                cipherIndex = (temp + key) % 26
            elif(encrypt == "decrypt"):
                 cipherIndex = (temp - key) % 26
            result +=chr(cipherIndex+65) 

    print(result)
    return result

CaesarCipher("TODAY IS A GOOD DAY", 7, "encrypt")
CaesarCipher("AVKHF PZ H NVVK KHF", 7, "decrypt")
#ord() input is a character, return the ascii code value of the input
#chr() input is an ascii value, return the chr 

#當不知道key等於多少的時候
for i in range(1,26):
    print(i)
    CaesarCipher("AVKHF PZ H NVVK KHF", i, "decrypt")