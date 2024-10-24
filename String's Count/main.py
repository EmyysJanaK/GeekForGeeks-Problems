class Solution:
    def countStr(self, n):
        dp0 = [0]*(n+1)
        dp1 = [0]*(n+1)
        dp2 = [0]*(n+1)

        dp0[1] = 1
        dp1[1] = 1
        dp2[1] = 1

        for i in range(2, n+1):
            dp0[i] = dp0[i-1]
            dp1[i] = dp0[i-1] + dp1[i-1]
            dp2[i] = dp0[i-1] + dp1[i-1] + 2*dp2[i-1]

        return dp0[n] + dp1[n] + dp2[n]


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.countStr(n))
