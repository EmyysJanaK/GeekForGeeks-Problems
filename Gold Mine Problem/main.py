def maxGold(n, m, M):
    dp = [[0 for j in range(m)] for i in range(n)]

    for j in range(m-1, -1, -1):
        for i in range(n):
            right = dp[i][j+1] if j+1 < m else 0
            right_up = dp[i-1][j+1] if i-1 >= 0 and j+1 < m else 0
            right_down = dp[i+1][j+1] if i+1 < n and j+1 < m else 0

            dp[i][j] = M[i][j] + max(right, right_up, right_down)

    max_gold = 0
    for i in range(n):
        max_gold = max(max_gold, dp[i][0])

    return max_gold

# Example 1
n1, m1 = 3, 3
M1 = [[1, 3, 3], [2, 1, 4], [0, 6, 4]]
print(maxGold(n1, m1, M1))  # Output: 12

# Example 2
n2, m2 = 4, 4
M2 = [[1, 3, 1, 5], [2, 2, 4, 1], [5, 0, 2, 3], [0, 6, 1, 2]]
print(maxGold(n2, m2, M2))  # Output: 16

# if __name__ == "__main__":
#     t = int(input())
#     for _ in range(t):
#         n, m = [int(x) for x in input().split()]
#         tarr = [int(x) for x in input().split()]
#         M = []
#         j = 0
#         for i in range(n):
#             M.append(tarr[j:j+m])
#             j += m
#         ob = Solution()
#         print(ob.maxGold(n, m, M))