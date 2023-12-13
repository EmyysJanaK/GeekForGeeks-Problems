#User function Template for python3
class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        # code here 
        max_sum = 0
        current_sum = 0

        for i in range(K,N):
            current_sum += Arr[i] - Arr[i-K]
            max_sum = max(max_sum, current_sum)
        
        return max_sum + sum(Arr[:K])

N = 4 
K = 4
Arr = [100, 200, 300, 400]
ob = Solution()
print(ob.maximumSumSubarray(K, Arr, N))  