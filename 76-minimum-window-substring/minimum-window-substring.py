class Solution:
    def isvalid(self, sourcemap, curmap):
        for key in sourcemap:
            if key not in curmap or curmap[key] < sourcemap[key]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        sourcemap = {}
        for ch in t:
            if ch in sourcemap:
                sourcemap[ch] += 1
            else:
                sourcemap[ch] = 1
        
        curmap = {}
        for i in range(0, len(t)):
            if s[i] in curmap:
                curmap[s[i]] += 1
            else:
                curmap[s[i]] = 1
        
        start = 0
        end = len(t) - 1
        curminlen = len(s) + 1
        ans = ""
        while True:
            isvalidstate = self.isvalid(sourcemap, curmap)

            if isvalidstate:
                if curminlen > end-start+1:
                    curminlen = min(curminlen,  end - start + 1)
                    ans = s[start:end+1]
                curmap[s[start]] -= 1
                start = start + 1
            else:
                end = end + 1
                if end >= len(s):
                    break
                if s[end] in curmap:
                    curmap[s[end]] += 1 
                else:
                    curmap[s[end]] = 1
        return ans