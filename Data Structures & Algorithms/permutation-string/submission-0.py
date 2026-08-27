class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s = set(s1)
        l =0
        while l< len(s2):
            if s2[l] in s:
                j = set(s2[l:l+len(s1)])
                # print(j,s)
                if s==j:
                    return True
            l+=1
        return False