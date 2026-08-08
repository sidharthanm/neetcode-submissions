class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1 :
            return 0
        l = 0
        r = 1

        res = 0
        while r<len(prices):
            if prices[l] <prices[r]:
                res = max(res,prices[r]-prices[l])
            else:
                l = r

            r+=1
        return res
        