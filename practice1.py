'''
P_67 Example:
Given an array of distinct integer values, count the number of pairs of integers that have difference k.
For example, give arr = {1, 7, 5, 9, 2, 12, 3} and k = 2, there are 4 pairs.
(1,3), (3,5), (5,7), (7,9)
'''

def p_67e_brute(arr, k):

    count = 0

    for item in arr:
        subArr = arr[arr.index(item)+1: len(arr)]

        for secItem in subArr:
            if(abs(item - secItem) == k):
                count = count + 1

    return count

def p_67e_optimized(arr, k):

    hashtable = {}
    count = 0

    for item in arr:
        if item in hashtable:
            hashtable[item] = hashtable[item] + 1
        else:
            hashtable[item] = 0

    for item in arr:
        diff = item - k

        if diff in hashtable:
            count = count + 1

    return count

def main():
    arr = [1, 7, 5, 9, 2, 12, 3]
    k = 2

    print("arr = " + str(arr))
    print("k = " + str(k))
    print(str(p_67e_brute(arr, k)) + " pairs were found using brute force.")
    print(str(p_67e_optimized(arr, k)) + " pairs were found using optimized.")

if __name__ == "__main__":
    main()