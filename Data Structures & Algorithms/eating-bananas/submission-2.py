class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        prev = r+1
        total = 0
        # time_max = float("inf")
        while l <= r:
            total = 0
            cur = l+((r-l)//2)
            for i in piles:
                total += math.ceil(float(i)/cur)
            
            if total<=h:
                prev = cur
                r = cur -1
            else:
                l = cur +1
            print(l,r,cur,prev,total)
        return prev

