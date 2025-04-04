class Solution:
    def maxProfit(self, prices):
        mx = 0
        mn = prices[0]

        for elem in prices:
            mx = max(mx, elem - mn)
            mn = min(mn, elem)
        return mx
