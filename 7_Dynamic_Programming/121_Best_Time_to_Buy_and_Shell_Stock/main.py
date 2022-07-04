class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        
        profit = 0
        boughtDay = 0
        minBoughtPrice = prices[0]
        for i in range(1, len(prices)):
            if prices[boughtDay] > prices[i]:
                boughtDay = i
                minBought = prices[i]
            iProfit =  prices[i] - prices[boughtDay]
            if iProfit > 0 and iProfit > profit:
                profit = iProfit
        return profit