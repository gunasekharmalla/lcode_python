class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0 
        mn = float('inf')
        mx = 0
        mx_p = 0
        for price in prices:
            if price < mn:
                mn = price 
            else:
                profit = price - mn 
                mx = max(mx, profit) 
        return mx
        