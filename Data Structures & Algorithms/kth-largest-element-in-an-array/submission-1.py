class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify_max(nums)
        print(nums)
        while k>0:
            res = heapq.heappop_max(nums)

            # print(nums)
            k-=1
        return res