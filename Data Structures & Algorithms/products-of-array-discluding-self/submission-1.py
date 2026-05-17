class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [1]*len(nums)
        for i in range(1,len(nums)):
            l[i] *= l[i-1] *nums[i-1]
        r = [1]*len(nums)
        for i in range(len(nums)-2,-1,-1):
            r[i] *= r[i+1] *nums[i+1]
        res = [i*j for i,j in zip(l,r)]
        return res
            