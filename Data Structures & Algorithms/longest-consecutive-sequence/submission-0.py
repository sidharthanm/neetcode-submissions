class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s= set(nums)
        r = set()
        ctr = 1
        m = 1
        for i in s:
            if i in r:
                continue
            while i+1 in s:
                ctr+=1
                i+=1
                r.add(i)
            m = max(ctr,m)
            ctr=1
        return m