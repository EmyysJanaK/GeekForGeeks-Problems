#Emmy'sjanak
class Solution:    
    def countOccurence(arr, n, k):
        counts = {}
        for element in arr:
            if element in counts:
                counts[element] += 1
            else:
                counts[element] = 1

        count = 0
        for element in counts:
            if counts[element] > n/k:
                count += 1

        return count

# drive code starts here
# import math
# def main():
#     T=int(input())
#     while(T>0):
#         I=[int(x) for x in input().strip().split()]
#         n=I[0]
#         k=I[1]
#         arr=[int(x) for x in input().strip().split()]
#         ob=Solution()
#         print(ob.countOccurence(arr,n,k))
#         T-=1


N = 4
arr = [2,3,3,2]
k = 3

print(Solution.countOccurence(arr, N, k))

N = 8
arr = [3,1,2,2,1,2,3,3]
k = 4

print(Solution.countOccurence(arr, N, k))