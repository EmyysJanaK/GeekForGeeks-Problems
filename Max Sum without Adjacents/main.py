#User function Template for python3

def findMaxSum(arr, n):
    incl = 0
    excl = 0
    for i in range(n):
        new_excl = max(incl, excl)
        incl = excl + arr[i]
        excl = new_excl
    return max(incl, excl)



arr = [3, 2, 7, 10, 4, 5, 6, 1, 2, 3, 4]

print(findMaxSum(arr, len(arr)))