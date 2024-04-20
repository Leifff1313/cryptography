import numpy as np

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

A = np.array([[3,5],[1,2]])
B = np.array([2,3])

def encrypt(plaintext):
    cipher = ""
    for i in range(0, len(plaintext),2):
        first_letter = plaintext[i]
        second_letter = plaintext[i+1]
        p1 = letters.find(first_letter)
        p2 = letters.find(second_letter)
        p = np.array([p1,p2])
        cipherVector = np.dot(A,p) + B 
        c1 = cipherVector[0] % 26
        c2 = cipherVector[1] % 26
        cipher += letters[c1]
        cipher += letters[c2]
    return cipher 

def decrypt(cipher):
    A_inverse = np.array([[2,-5],[-1,3]])
    plaintext = ""
    for i in range(0, len(cipher),2):
        first_letter = cipher[i]
        second_letter = cipher[i+1]
        c1 = letters.find(first_letter)
        c2 = letters.find(second_letter)
        c = np.array([c1,c2])
        plaintextVector = np.dot(A_inverse, c) - np.dot(A_inverse, B)
        p1 = plaintextVector[0] % 26
        p2 = plaintextVector[1] % 26
        plaintext += letters[p1]
        plaintext += letters[p2]
    return plaintext




print(encrypt("HELPSAVEME"))
print(decrypt("RSGSEVHGGX"))
#因為是兩個兩個切字串，所以字串要是偶數程式才能跑