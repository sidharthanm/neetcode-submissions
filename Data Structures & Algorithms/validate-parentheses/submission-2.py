class Solution:
    def isValid(self, s: str) -> bool:
        d = []
        for i in s:
            if i in "([{":
                d.append(i)
            else:
                if not d:
                    return False
                a = d.pop()
                
                if a == "{" and i !="}":
                     return False
                elif a =="[" and i!="]":
                    return False
                elif a == "(" and i!=")":
                    return False
        if d:
            return False 
        else: 
            return True