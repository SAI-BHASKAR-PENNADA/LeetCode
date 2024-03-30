class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        charmap = {}
        ans = 0
        start = 0
        for i in range(len(s)):
            if s[i] not in charmap:
                ans = max(ans, i - start + 1)
            else:
                index = charmap[s[i]]
                if start <= index:
                    start = index + 1
                ans = max(ans, i - start + 1)
            charmap[s[i]] = i
        return ans