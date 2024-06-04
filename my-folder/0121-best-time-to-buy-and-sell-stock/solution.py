class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, min_buy = 0, float("inf")

        for price in prices:
            profit = max(profit, price - min_buy)
            min_buy = min(price, min_buy)
        
        return profit
