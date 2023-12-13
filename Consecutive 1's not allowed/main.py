class Solution:
    def countStrings(self, N):
        MOD = 10**9 + 7

        ends_with_zero = [0] * (N + 1)
        ends_with_one = [0] * (N + 1)

        ends_with_zero[1] = 1
        ends_with_one[1] = 1

        for i in range(2, N + 1):
            ends_with_zero[i] = (ends_with_zero[i - 1] + ends_with_one[i - 1]) % MOD
            ends_with_one[i] = ends_with_zero[i - 1] % MOD

        return (ends_with_zero[N] + ends_with_one[N]) % MOD