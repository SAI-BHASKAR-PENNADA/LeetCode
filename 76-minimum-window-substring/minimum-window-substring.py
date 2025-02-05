class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = ""
        start = 0
        end = 0

        tmap = {}
        for ch in t:
            if ch not in tmap:
                tmap[ch] = 1
            else:
                tmap[ch] += 1
        
        count = 0
        def isValid():
            if end - start + 1 < len(t):
                return False
            
            return count == len(tmap)

        addEnd = True
        while end < len(s):
            if addEnd:
                if s[end] in tmap:
                    tmap[s[end]] -= 1
                    if tmap[s[end]] == 0:
                        count += 1

            if not isValid():
                end += 1
                addEnd = True
            else:
                if end - start + 1 < len(ans) or ans == "":
                    ans = s[start:end+1]
                if s[start] in tmap:
                    tmap[s[start]] += 1
                    if tmap[s[start]] == 1:
                        count -= 1
                start += 1
                addEnd = False

        return ans
        