class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        s = [0]*26
        for word in words:
            for letter in word:
                s[ord(letter)-ord("a")] +=1
        print(s)

        
        for i in s:
            if i%len(words)!=0:
                return False
        return True