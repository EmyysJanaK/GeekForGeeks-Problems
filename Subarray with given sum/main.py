#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self, arr, n, s): 
        current_sum = arr[0]
        start = 0

        for end in range(1, n+1):
            while current_sum > s and start < end-1:
                current_sum = current_sum - arr[start]
                start += 1

            if current_sum == s:
                return [start + 1, end]

            if end < n:
                current_sum = current_sum + arr[end]

        return [-1]
        
# # driver code starts
# import math

# def main():
#     T = int(input())
#     while(T > 0):
#         NS = input().strip().split()
#         N = int(NS[0])
#         S = int(NS[1])
#         A = [int(x) for x in input().strip().split()]
#         ob=Solution()
#         ans=ob.subArraySum(A, N, S)
#         for i in ans:
#             print(i, end=" ")
#         print()
#         T -= 1
# if __name__ == "__main__":
#     main()

# # } Driver Code Ends