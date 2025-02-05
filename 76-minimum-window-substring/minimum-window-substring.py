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
        
        smap = {}
        def isValid():
            if end - start + 1 < len(t):
                return False
            # print(smap, tmap)
            valid = True
            for ch in tmap:
                if ch not in smap or tmap[ch] > smap[ch]:
                    valid = False
                    break
            return valid

        addEnd = True
        while end < len(s):
            if addEnd:
                if s[end] not in smap:
                    smap[s[end]] = 1
                else:
                    smap[s[end]] += 1

            if not isValid():
                end += 1
                addEnd = True
            else:
                if end - start + 1 < len(ans) or ans == "":
                    ans = s[start:end+1]
                smap[s[start]] -= 1
                start += 1
                addEnd = False
        
        # if isValid() and  (end - start < len(ans) or ans == ""):
        #     # print("test", start, end)
        #     ans = s[start:end]

        return ans
        