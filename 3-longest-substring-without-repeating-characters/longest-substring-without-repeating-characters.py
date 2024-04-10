class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if len(s) == 0:
        #     return 0

        # charmap = {}
        # ans = 0
        # start = 0
        # for i in range(len(s)):
        #     if s[i] not in charmap:
        #         ans = max(ans, i - start + 1)
        #     else:
        #         index = charmap[s[i]]
        #         if start <= index:
        #             start = index + 1
        #         ans = max(ans, i - start + 1)
        #     charmap[s[i]] = i
        # return ans

        if not s:
            return 0

        i = 0
        j = 1
        ans = 1
        charmap = {}
        charmap[s[i]] = 0
        while j < len(s):
            if s[j] in charmap:
                while i < j:
                    if s[i] == s[j]:
                        break
                    else:
                        del charmap[s[i]]
                    i += 1
                i += 1
                j += 1
            else:
                ans = max(ans, j - i + 1)
                charmap[s[j]] = 0
                j += 1
        return ans