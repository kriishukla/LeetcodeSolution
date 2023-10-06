class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = {}

        def fn(i, buying):
            if i >= n:
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            if buying:
                buy = fn(i + 1, not buying) - prices[i]
                cooldown = fn(i + 1, buying)
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = prices[i] + fn(i + 2, not buying)
                cooldown = fn(i + 1, buying)
                dp[(i, buying)] = max(sell, cooldown)
            
            return dp[(i, buying)]
        
        return fn(0, True)