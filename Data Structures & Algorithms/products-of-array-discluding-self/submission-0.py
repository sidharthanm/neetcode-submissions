class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [1]* len(nums)
        cur = 1
        for i in range(len(nums)):
            l[i] *=cur
            cur *= nums[i]
        cur = 1
        for i in range(len(nums)-1,-1,-1):
            l[i] *=cur
            cur *= nums[i]
        
        return l
        