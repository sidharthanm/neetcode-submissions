class Solution:
    def minWindow(self, s: str, t: str) -> str:
        have = 0
        need = len(set(t))
        count = {}
        final = {}
        res =(1,10001)
        for i in t:
            final[i] = final.get(i,0) +1 
        t = set(t)
        l = -1
        for i in range(len(s)):
            if s[i] in t:
                l = i
                break
        print(l)
        if l == -1:
            return ""        
        r = l
        if len(t)>len(s):
            return ""
        while r<len(s):
            if s[r] in t:
                count[s[r]] = count.get(s[r],0) +1
                if count[s[r]] == final[s[r]]:
                    have+=1
                
            while have == need:
                if (r-l) < res[1]-res[0]:
                    res = (l,r)
                
                if s[l] in count:
                    count[s[l]] -= 1
                if s[l] in count and count[s[l]] < final[s[l]]:
                    have -= 1
                l+=1
                while s[l] not in count and l<=r:
                    l+=1
            r+=1
        print(l)
        l,r = res
        print(l)
        return s[l:r+1] if res[1] != 10001 else ""




