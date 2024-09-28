class Solution:
    def isvalid(self, stringmap, k, stringlength):
        mostRep = max(stringmap.values())
        return mostRep + k >= stringlength

    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0
        
        ans = 0
        start, end = 0, 0
        stringmap = {}
        stringmap[s[0]] = 1
        while end < len(s):
            # if state is valid: increment end, else: increment start
            if self.isvalid(stringmap, k, end-start+1):
                ans = max(ans, end-start+1)
                end = end + 1
                if end >= len(s):
                    break
                if s[end] in stringmap:
                    stringmap[s[end]] += 1
                else:
                    stringmap[s[end]] = 1
            else:
                # print(start)
                stringmap[s[start]] -= 1
                start = start + 1
            # print(stringmap)
        ans = max(ans, end-start)
        return ans