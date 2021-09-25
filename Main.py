from math import sqrt
import numpy as np

def keyMatrixConstruction(key):
    keyMatrix = []
    count = 0
    rows, cols = (int(sqrt(len(key))), int(sqrt(len(key))))
    for i in range(rows):
        col = []
        for j in range(cols):
            col.append(ord(key[count])-65)
            count += 1
        keyMatrix.append(col)    
    return keyMatrix

def stringMatrixConstruction(string):
    stringMatrix = []
    count = 0
    rows, cols = (3,1)
    for i in range(rows):
        col = []
        for j in range(cols):
            col.append(ord(string[count])-65)
            count += 1
        stringMatrix.append(col)
    return stringMatrix

def matrixMultiplication(stringMatrix, keyMatrix):
    keyMatrix = np.array(keyMatrix)
    stringMatrix = np.array(stringMatrix)
    res = np.matmul(keyMatrix, stringMatrix)
    encryptedString = res % 26
    return encryptedString

if __name__ ==  "__main__":

    string = input("Enter a string : ")
    key = input("Enter a key : ")
    encryptedString = matrixMultiplication(stringMatrixConstruction(string), keyMatrixConstruction(key))
    print("Encrypted String : ", encryptedString)
