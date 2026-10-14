class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [1, 2]
        dp = [0] * (n+1) #[1, 0, 0, 0]
        dp[0] = 1

        for i in range(1, n+1):
            for s in steps:
                if i - s >= 0:
                    dp[i] += dp[i - s]
        return dp[n]


        