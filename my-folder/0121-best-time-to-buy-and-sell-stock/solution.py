class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = float('-inf')
        min_buy = float('inf')

        for price in prices:
            max_profit = max(max_profit, price - min_buy)
            min_buy = min(min_buy, price)
        
        return max_profit if max_profit > 0 else 0
