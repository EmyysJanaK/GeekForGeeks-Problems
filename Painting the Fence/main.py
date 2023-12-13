class Solution:
    def countWays(self, n, k):
        if n == 0: return 0
        elif n == 1: return k
        same, diff = k, k * (k - 1)
        mod_val = 10**9 + 7
        for i in range(3, n + 1):
            same, diff = diff, (same + diff) * (k - 1) % mod_val
        return (same + diff) % mod_val