class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        
        cur_max = 0
        prev = nums[0]
        track = 1 
        for i in range(1,len(nums)):
            # print(nums[i],track)
            if nums[i] == prev:
                pass 
            elif nums[i] == prev+1:
                track+=1
            else:
                cur_max = max(track,cur_max)
            prev =  nums[i]
        cur_max = max(track,cur_max)
        return cur_max