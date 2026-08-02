class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def check(s, d,t):
            cur_el = set(d.keys())
            print(cur_el,s.issubset(cur_el))
            print(d,t)
            if not cur_el :
                return False
            for i in t.keys():
                if i not in d or d[i] < t[i]:
                    return False
                    
            return True

        ts = set(t)
        sd = dict()
        td = dict()
        for i in t:
            if i in td:
                td[i] += 1
            else:
                td[i] = 1
        
        res = []
        track = dict()
        l = 0
        while l < len(s) and s[l] not in ts:
            l += 1
        r =l 

        while r < len(s):
            if s[r] in ts:
                if s[r] in sd:
                    sd[s[r]] += 1
                else:
                    sd[s[r]] = 1

                if check(ts, sd,td):
                    if not res:
                        res = (l, r)
                    else:
                        a, b = res
                        if (b - a) > (r - l):
                            res = (l,r)
                    while check(ts,sd,td) and l<=r:
                        res = (l,r) if r-l < res[1]-res[0] else res
                        print(sd,l)
                        if s[l] in ts:
                            if sd[s[l]] == 1:
                                del sd[s[l]]
                            else:
                                sd[s[l]] -= 1
                        l+=1
                    while l<=r and (s[l] not in ts):
                        l+=1 
            r+=1
            print(l,r)
        print(res)
        if res:
            return s[res[0]:res[1]+1]
        return ""
                

                        