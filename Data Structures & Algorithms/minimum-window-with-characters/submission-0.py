class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def check(s, d):
            cur_el = set(d.keys())
            print(cur_el,s.issubset(cur_el))
            return s.issubset(cur_el)

        ts = set(t)
        td = dict()
        # for i in t:
        #     if i in td:
        #         td[i] += 1
        #     else:
        #         td[i] = 1
        
        res = []
        track = dict()
        l = 0
        r = 0

        while r < len(s):
            if s[r] in ts:
                if s[r] in td:
                    td[s[r]] += 1
                else:
                    td[s[r]] = 1

                if check(ts, td):
                    if not res:
                        res = (l, r)
                    else:
                        a, b = res
                        if (b - a) > (r - l):
                            res = (l,r)
                    while check(ts,td) and l<=r:
                        print(td,l)
                        if s[l] in ts:
                            if td[s[l]] == 1:
                                del td[s[l]]
                            else:
                                td[s[l]] -= 1
                        l+=1
                    while l<r and (s[l] not in ts):
                        l+=1 
            r+=1
        print(res)
        if res:
            return s[res[0]:res[1]+1]
        return ""
                

                        