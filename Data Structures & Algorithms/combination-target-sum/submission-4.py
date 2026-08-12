class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        visited = {}
        res = []
        def fill(cur,val):
            if val in visited:
                if val== False:
                    return
                for i in visited[val]:
                    copy = cur[:]
                    copy.extend(i)
                    # print(i,copy,val)
                    res.append(copy)
                return
            
            if val == 0:
                # print(val,cur)
                res.append(cur[:])
                return
            if val<0:
                return
            
            for i in nums:
                cur.append(i)
                fill(cur,val-i)
                cur.pop()
            return
        
        for i in range(1,target+1):
            res =[]
            fill([],i)
            if res == []:
                visited[i] = False
            s = set()
            # print(res)
            for r in res:
                r.sort()
                s.add(tuple(r))
            res = [list(q) for q in s]
            visited[i] = res[:]

        # print(visited)
        return visited[target]


                    