class Solution:

    def encode(self, strs: List[str]) -> str:
        r =  ''
        for i in strs:
            r+=f'{len(i)}#{i}'
        print(r)
        return r
    def decode(self, s: str) -> List[str]:
        words =[]
        lp = 0
        while lp < len(s):
            tmpn = ''
            while s[lp] !='#':
                tmpn += s[lp]
                lp+=1
            lp+=1
            cur=''
            tmpn = int(tmpn)
            while tmpn>0:
                cur+= s[lp]
                tmpn-=1
                lp+=1
            
            words.append(cur)
        return words
            

