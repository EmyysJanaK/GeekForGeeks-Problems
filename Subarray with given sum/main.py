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
