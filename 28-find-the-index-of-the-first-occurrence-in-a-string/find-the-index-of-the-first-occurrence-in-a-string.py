class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        
        i, j = 0, 0 

        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                i = i - j + 1
                j = 0

        if j == len(needle):
            return i - len(needle)
        return -1