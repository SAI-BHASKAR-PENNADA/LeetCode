class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        if len(pattern) != len(words):
            return False
        
        bijection = {}
        wordSet = set()
        for i in range(len(words)):
            if pattern[i] not in bijection:
                if words[i] in wordSet:
                    return False
                bijection[pattern[i]] = words[i]
                wordSet.add(words[i])
            else:
                if bijection[pattern[i]] != words[i]:
                    return False
        return True