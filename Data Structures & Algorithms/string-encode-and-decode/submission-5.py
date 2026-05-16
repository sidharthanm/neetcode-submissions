class Solution:

    def encode(self, strs: List[str]) -> str:
        l = ''
        for i in strs:
            l += str(len(i))+"#"+i
        print(l)
        return l

    def decode(self, s: str) -> List[str]:
        if len(s) ==0:
            return []
        ptr = 0
        res =[]
        while ptr<len(s)-1:
            l = ptr
            position =''
            while s[ptr]!= '#':
                position+=s[ptr]
                ptr+=1
            position = int(position)
            ptr+=1
            res.append(s[ptr:ptr+position])
            ptr = ptr+position
        
        return res

        