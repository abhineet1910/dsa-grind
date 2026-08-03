class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0 
        best_buy=prices[0]
        n = len(prices)
        for i in range(1,n):
            if prices[i]>best_buy:
                max_profit=max(max_profit,prices[i]-best_buy)
            best_buy=min(best_buy,prices[i])
        return max_profit
        """
        :type prices: List[int]
        :rtype: int
        """
        