'''
Check Permutation:
Given 2 strings, write a method to decide if one is a permutation of the other.
'''

def checkPermutation(strVar1, strVar2):
    hashTable = {}

    if len(strVar1) != len(strVar2):
        return False

    for item in strVar1:
        if item in hashTable:
            hashTable[item] = hashTable[item] + 1
        else:
            hashTable[item] = 1

    #print(str(hashTable))

    for item in strVar2:
        if item in hashTable:
            if hashTable[item] == 0:
                return False
            hashTable[item] = hashTable[item] - 1
        else:
            return False

    return True

def main():
    str1 = "abcd"
    str2 = "dcba"
    str3 = "bcae"

    print(str( checkPermutation(str1, str2) ))
    print(str( checkPermutation(str1, str3) ))

if __name__ == "__main__":
    main()