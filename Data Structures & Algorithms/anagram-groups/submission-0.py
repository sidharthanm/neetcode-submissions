class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        track = dict()
        for word in strs:
            l = [0]*26
            for letter in word:
                l[ord('a')-ord(letter)] +=1
            l = tuple(l)
            if l in track:
                track[l].append(word)
            else:
                track[l] = [word,]
        
        return list(track.values())