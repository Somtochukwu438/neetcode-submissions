class Solution:
    def climbStairs(self, n: int) -> int:
        arr = {0: 1, 1: 1}
        def helper(n):
            if n in arr: 
                return arr[n]
            ans = helper(n - 1) + helper(n - 2)
            arr[n] = ans
            return arr[n] 
        return helper(n) 