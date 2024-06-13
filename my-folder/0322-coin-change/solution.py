from typing import Dict
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = self.dfs(coins, amount, dict())
        return res if res != float("inf") else -1

    def dfs(self, coins: List[int], amount: int, cache: Dict[int, int]):
        if amount in cache:
            return cache[amount]
        elif amount == 0:
            return 0
        elif amount < 0:
            return float("inf")
        else:
            min_coins = float("inf")
            cache[amount] = min([1 + self.dfs(coins, amount - coin, cache) for coin in coins])
            return cache[amount]
