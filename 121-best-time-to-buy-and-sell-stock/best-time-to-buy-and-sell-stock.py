class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0

        bestprice = [0]*len(prices)
        bestprice[-1] = prices[-1]
        for i in range(len(prices) - 2, -1, -1):
            bestprice[i] = max(prices[i], bestprice[i+1])

        
        for i in range(len(prices) - 1):
            ans = max(ans, bestprice[i+1] - prices[i])
        return ans