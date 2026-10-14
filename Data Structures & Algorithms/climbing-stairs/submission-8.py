class Solution:
    def climbStairs(self, n: int) -> int:
        step = [1, 2]
        dp = [0] * (n+1)
        dp[0] = 1

        for i in range(1, n+1):
            for c in step:
                if i - c >= 0:
                    dp[i] += dp[i-c]
        return dp[n]
        
        