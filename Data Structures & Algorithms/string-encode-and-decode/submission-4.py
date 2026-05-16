class Solution:

    def encode(self, strs: List[str]) -> str:
        l = ''
        for i in strs:
            l += str(len(i))+i
        print(l)
        return l

    def decode(self, s: str) -> List[str]:
        if len(s) ==0:
            return []
        l = int(s[0])
        res = []
        ptr = 1
        while ptr<=len(s):
            print(ptr,l)
            res.append(s[ptr:l+ptr])
            ptr += l
            if ptr<len(s):
                l = int(s[ptr])
            ptr+=1
        
        print(ptr,l)
        return res