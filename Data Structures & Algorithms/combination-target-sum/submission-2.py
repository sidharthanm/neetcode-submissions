class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:


        res = []
        visited =set()
        def rec(cur,val):
            # print(cur,val)
            if val>target:
                # cur.pop()
                return
            if val == target:
                cop = cur[:]
                cop.sort()
                if tuple(cop) in visited:
                    return
                
                res.append(cop)
                visited.add(tuple(cop))


                # cur.pop()
                return

            for i in nums:
                if val+i>target:
                    continue
                cur.append(i)
                rec(cur,val+i)
                cur.pop()
        
        rec([],0)

        return res