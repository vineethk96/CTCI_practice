'''
Example: Print all positive integer solutions to the equation (a^3) + (b^3) = (c^3) + (d^3)
where a, b, c, and d are integers between 1 and 1000
'''

# brute force method would be 4 loops, 1 for each variable

def p_68e(n):

    hashMap = {}

    for a in range(n):
        for b in range(n):
            leftSide = (a**3) + (b**3)
            hashMap.update({ leftSide: (a,b) })
            #print(hashMap[leftSide])

    for item in hashMap:
        #print(str(item) + ":" + str(hashMap[item]))
        print("Pairs:")
        for pair in hashMap[item]:
            for secPair in hashMap[item]:
                print("(" + str(pair) + ", " + str(secPair) + ")")

def main():
    n = 10

    p_68e(n)


if __name__ == "__main__":
    main()
