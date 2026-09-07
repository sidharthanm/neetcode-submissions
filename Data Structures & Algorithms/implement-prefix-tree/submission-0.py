class TrieNode:
    def __init__(self,):
        self.values = dict()
        self.isendofword = False
        
class PrefixTree:

    def __init__(self):
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.values:
                cur.values[c] = TrieNode()
            cur = cur.values[c]
        cur.isendofword = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c  in word:
            if c not in cur.values:
                return False
            cur = cur.values[c]
        return cur.isendofword

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c  in prefix:
            if c not in cur.values:
                return False
            cur = cur.values[c]
        return True
        