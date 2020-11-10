'''
Is Unique
Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional structures?
'''

def isUnique(charArray):
    hashTable = {}

    for item in charArray:
        if item in hashTable:
            return False
        else:
            hashTable[item] = "0"
    return True

def isUnique_noDS():



    return True

def main():
    str1 = ".abcde0fg"
    str2 = "aabbccdd"

    if isUnique(str1):
        print("str1 is unique")
    else:
        print("str1 is not unique")

    if isUnique(str2):
        print("str2 is unique")
    else:
        print("str2 is not unique")

if __name__ == "__main__":
    main()