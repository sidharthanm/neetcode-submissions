class Solution:
    def trap(self, height: List[int]) -> int:
        le = len(height)
        maxl = [0] * le
        maxr = [0] * le
        res = 0
        a = 0
        r = height[le - 1]
        l = height[0]
        while a<le:
            maxl[a] = l
            l  = max(height[a],l)
            maxr[le-a-1] = r
            r = max(height[le-a-1],r)
            a+=1
        a = 0
        print(maxl)
        print(maxr)
        print(height)
        while a<le:
            res+= (min(maxl[a],maxr[a]) -height[a])if(min(maxl[a],maxr[a]) -height[a])>0 else 0
            a+=1
        return res

