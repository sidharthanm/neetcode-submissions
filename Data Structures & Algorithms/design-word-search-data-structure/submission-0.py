class TrieNode:
    def __init__(self):
        self.values = dict()
        self.isendofword = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

        

    def addWord(self, word: str) -> None:
        cur  = self.root
        for c in word:
            if c not in cur.values:
                cur.values[c] = TrieNode()
            cur = cur.values[c]
        cur.isendofword =True

    def search(self, word: str) -> bool:
        cur = self.root
        track = [False]
        def rec(cur,word,s,track):
            if track[0]:
                return True
            if s>=len(word):
                track[0] = True
                return True
            
            if word[s] == '.' and s==len(word)-1:
                track[0] =True
                return True

            if word[s] == '.':
                for c  in cur.values:
                    rec(cur.values[c],word,s+1,track)

            for c in word[s:]:
                if c not in cur.values:
                    return False
                rec(cur.values[c],word,s+1,track)
        rec(cur,word,0,track)
        return track[0]
                

