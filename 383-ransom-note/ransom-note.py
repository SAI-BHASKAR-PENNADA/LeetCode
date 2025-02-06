class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        store = {}
        for ch in magazine:
            if ch in store:
                store[ch] += 1
            else:
                store[ch] = 1
        
        for ch in ransomNote:
            if ch not in store or store[ch] == 0:
                return False
            store[ch] -= 1
        return True