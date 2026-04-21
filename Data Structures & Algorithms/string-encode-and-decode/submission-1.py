class Solution:

    def encode(self, strs: List[str]) -> str:
        s =[]
        for i in strs:
            s.append(str(len(i)))
            s.append("#")
            s.extend(i)
        return ''.join(s)
    def decode(self, s: str) -> List[str]:
        l =[]
        p = 0
        print(s)
        while p<len(s):
            print(p)
            r = 0
            i=[]
            while True:
                r+=1
                i.append(s[p])    
                p+=1
                if s[p]=='#':
                    break
                
                #i = int(s[p])
            i = int(''.join(i))
            #print("i",s[p])
            print(s[p+1:i+1])
            q = s[p+1:p+i+1]
            p += i+1
            print(q)
            l.append(q)
        return l