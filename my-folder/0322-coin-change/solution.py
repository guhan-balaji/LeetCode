class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def cc(amount: int) -> int:
            if amount in coins:
                return 1
            elif amount == 0:
                return 0
            elif amount < 0:
                return float("inf")
            else:
                return min([1 + cc(amount - coin) for coin in coins])
                # print(min_coins)
                # return min_coins if min_coins != float("inf") else -1

        return cc(amount) if cc(amount) != float("inf") else -1
            

