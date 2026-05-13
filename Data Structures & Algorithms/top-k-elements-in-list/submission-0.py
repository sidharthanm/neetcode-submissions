class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_dict = dict()
        for i in nums:
            if i not in counter_dict:
                counter_dict[i] = 1
            else:
                counter_dict[i]+=1
        
        res = dict()
        for key,value in counter_dict.items():
            if value in res :
                res[value].append(key)
            else:
                res[value] = [key,]
        x =sorted(list(set(counter_dict.values())),reverse= True)
        result = []
        m = k
        for i in range(k):
            if m:
                result.extend(res[x[i]])
                m-=len(res[x[i]])
            else:
                break
        return result