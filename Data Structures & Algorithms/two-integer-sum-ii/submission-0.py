class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        track = dict()

        for i in range(len(numbers)):
            if numbers[i] in track:
                return [track[numbers[i]]+1,i+1]
            
            track[target-numbers[i]] = i

            
