class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        if len(nums) == 0:
            return 0
        if len(nums) ==1:
            return 1
        cur_max = 0
        prev = nums[0]
        track = 1 
        for i in range(1,len(nums)):
            print(nums[i],track)
            if nums[i] == prev:
                pass 
            elif nums[i] == prev+1:
                track+=1
            else:
                cur_max = max(track,cur_max)
                track = 1
            prev =  nums[i]
        cur_max = max(track,cur_max)
        return cur_max