class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicts = {}
        for ch in s:
            if ch in dicts:
                dicts[ch] += 1
            else:
                dicts[ch] = 1
        
        for ch in t:
            if ch not in dicts:
                return False
            else:
                dicts[ch] -= 1
                if dicts[ch] == 0:
                    del dicts[ch]

        return len(dicts) == 0