class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()
        for i in nums:
            if i in nums:
                if i in d:
                    d[i]+=1
                else:
                    d[i] = 1
        
        
        resd = dict()

        for key,value in d.items():
            if value in resd:
                resd[value].append(key)
            else:
                resd[value] = [key]
        
        res = []
        for key,values in resd.items():
            res.append([key,values])

        x = sorted(list(d.values()),reverse = True)

        # print(res)
        # res.sort(reverse=True, key = lambda x: x[0])
        # print(res)
        print(x)
        m = k
        r = []
        for i in range(k):
            if m>0:
                r.extend(resd[x[i]])
            else:
                break
            m-=len(resd[x[i]])
        
        return r[:k]