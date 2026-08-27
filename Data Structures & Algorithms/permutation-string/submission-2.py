class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s = set(s1)
        l =0
        test = [0]*26
        for i in s1:
            test[ord(i)-ord("a")] +=1

        while l< len(s2):
            if s2[l] in s:
                j = [0]*26
                for c in s2[l:l+len(s1)]:
                    j[ord(c)-ord("a")]+=1
                # j = set(s2[l:l+len(s1)])
                # print(j,s)
                if test==j:
                    return True
            l+=1
        return False