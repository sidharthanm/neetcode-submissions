class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def rec(i,cur,left):
            if left == target:
                res.append(cur[:])
                return
            if i >= len(candidates) or left + candidates[i] > target:
                return
           
            cur.append(candidates[i])
            rec(i+1,cur[:],left+candidates[i])
            cur.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            rec(i+1,cur[:],left)
        rec(0,[],0)

        return res