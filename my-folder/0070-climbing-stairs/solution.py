class Solution:
    def climbStairs(self, n: int, memo = {}) -> int:
        if n in memo:
            return memo[n]
        else:
            if n == 0:
                return 1
            elif n < 0:
                return 0
            else:
                memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
                return memo[n]
