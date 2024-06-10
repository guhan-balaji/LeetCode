from typing import Dict
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            ways = [0] * n
            ways[0] = 1
            ways[1] = 2

            for i in range(2, n):
                ways[i] = ways[i - 1] + ways[i - 2]

            return ways[n - 1]
    #     return self.rec(n, dict())

    # def rec(self, n: int, memo: Dict[int, int] = dict()):
    #     if n < 1:
    #         return 0
    #     elif n == 1:
    #         return 1
    #     elif n == 2:
    #         return 2
    #     elif n in memo:
    #         return memo[n]
    #     else:
    #         memo[n] = self.rec(n - 1) + self.rec(n - 2)
    #         return memo[n]
