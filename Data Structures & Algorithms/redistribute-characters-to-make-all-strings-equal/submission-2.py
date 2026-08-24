class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counter = {}
        for word in words:
            for letter in word:
                if letter in counter:
                    counter[letter]+=1
                else:
                    counter[letter] = 1
        print(counter)


        for value in counter.values():
            if value%len(words)!=0:
                return False
        return True