class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1

        m = 0
        while l<r:
            m = max(min(heights[l],heights[r])*(r-l),m)
            if heights[l]<=heights[r]:
                l+=1
            else:
                r-=1
        return m
