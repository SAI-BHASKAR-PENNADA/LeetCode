class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # smap = {}
        # for ch in s:
        #     if ch not in smap:
        #         smap[ch] = 1
        #     else:
        #         smap[ch] += 1
        
        return "".join(sorted(s)) == "".join(sorted(t))