#User function Template for python3


class Solution:
    def missingNumber(self, array, n):
        total = n * (n + 1) // 2
        return total - sum(array)


# Driver Code Starts

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ob = Solution().missingNumber(a,n)
    print(ob)
# Driver Code Ends