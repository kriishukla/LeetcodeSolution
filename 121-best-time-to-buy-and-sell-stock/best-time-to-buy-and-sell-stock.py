class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr=prices[0]
        ans=0
        for i in range(len(prices)):
            curr=min(curr,prices[i])
            ans=max(prices[i]-curr,ans)
        
        return ans

        