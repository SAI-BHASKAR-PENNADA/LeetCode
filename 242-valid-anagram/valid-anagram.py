class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        smap = {}
        for ch in s:
            if ch not in smap:
                smap[ch] = 1
            else:
                smap[ch] += 1
        
        # count = len(smap)
        for ch in t:
            if ch not in smap or smap[ch] == 0:
                return False
            smap[ch] -= 1
        return True

        # return "".join(sorted(s)) == "".join(sorted(t))