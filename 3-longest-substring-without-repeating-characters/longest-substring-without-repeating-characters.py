class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0

        charmap = {}
        ans = 0
        while end < len(s):
            if s[end] not in charmap:
                charmap[s[end]] = end
            else:
                ans = max(ans, end-start)
                updatedStart = charmap[s[end]] + 1
                while start != updatedStart:
                    del charmap[s[start]]
                    start += 1
                charmap[s[end]] = end
            end += 1
        ans = max(ans, end-start)
        return ans
