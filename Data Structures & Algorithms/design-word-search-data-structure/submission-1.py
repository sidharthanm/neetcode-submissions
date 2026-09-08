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
        def rec(cur, s):
            # Finished processing the search word
            if s == len(word):
                return cur.isendofword

            c = word[s]

            # Wildcard: try every possible character
            if c == '.':
                for child in cur.values.values():
                    if rec(child, s + 1):
                        return True

                return False

            # Normal character doesn't exist
            if c not in cur.values:
                return False

            # Continue to next character
            return rec(cur.values[c], s + 1)

        return rec(self.root, 0)