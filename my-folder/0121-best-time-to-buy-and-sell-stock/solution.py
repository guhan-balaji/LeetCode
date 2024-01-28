class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0

        max_profit = 0
        buy = prices[0]
        for price in prices:
            max_profit = max(price - buy, max_profit)
            buy = min(price, buy)
        return max_profit
        
        """
        :type prices: List[int]
        :rtype: int
        """
        
