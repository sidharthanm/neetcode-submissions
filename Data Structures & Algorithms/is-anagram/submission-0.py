class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l = [0]*26
        r = [0]*26
        for i in s:
            l[ord('a') - ord(i)] += 1
        for i in t:
            r[ord('a') - ord(i)] += 1
        if tuple(l)==tuple(r):
            return True
        return False   
    
    