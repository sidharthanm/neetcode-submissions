class Solution:
    def minWindow(self, s: str, t: str) -> str:
        have,need = 0, len(t)
        countT, window = {},{}
        if len(s)<len(t):
            return ""
        for i in t:
            countT[i] = 1+ countT.get(i,0)
        t = set(t)
        need = len(t)
        l = -1
        res , reslen = [-1,-1],float("inf")
        for i in range(len(s)):
            if s[i] in countT:
                l = i
                break
        
        r = l
        while r<len(s):
            c = s[r]
            if c in t:
                window[c] = 1 + window.get(c,0)

                if countT[c] ==  window[c]:
                    have+=1
                
                print(l,r,c,window,countT,have,need)    
                while have == need:
                    if r-l+1 < reslen:
                        res = [l,r]
                        reslen = r-l+1

                    if s[l] in window:
                        window[s[l]] -= 1
                        if window[s[l]] < countT[s[l]]:
                            have -=1
                        
                    l+=1
                    while l<r and s[l] not in t:
                        l+=1
            r+=1
        if reslen >100000:
            return ""
        l,r = res
        return s[l:r+1]
                     

            

