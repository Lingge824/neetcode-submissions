class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        b,s=0,1
        while s<len(prices):
            if prices[b]<prices[s]:
                profit=prices[s]-prices[b]
                maxprofit=max(maxprofit,profit)
            else:
                b=s
            s+=1
        return maxprofit
        