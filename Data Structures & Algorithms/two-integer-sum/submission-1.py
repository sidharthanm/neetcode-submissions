class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = dict()
        for i in range(len(nums)):
            
            if nums[i] in a:
                return [ a[nums[i]],i]
            a[target-nums[i]] = i
            
        
            
