class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        f =[]
        res = []
        def rec(i,res):
            if i == len(nums):
                f.append(list(res))
                return
            res.append(nums[i])
            rec(i+1,res)
            res.pop()
            rec(i+1,res)
        rec(0,res)
        return f