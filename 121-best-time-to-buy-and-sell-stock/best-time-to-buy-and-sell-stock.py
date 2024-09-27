class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxarr = [0, prices[-1]]
        for i in range(len(prices) - 3, -1, -1):
            maxarr.append(max(maxarr[-1], prices[i+1]))
        maxarr.reverse()

        ans = 0
        for i in range(0, len(prices)):
            profit = maxarr[i] - prices[i]
            ans = max(ans, profit)
        return ans 