class Solution:
    def expand(self, s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i = i - 1
            j = j + 1
        return [i+1, j-1]

    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = 0
        for i in range(0, len(s)):
            # odd length palindromes
            help = self.expand(s, i, i)
            if end-start < help[1]-help[0]:
                start = help[0]
                end = help[1]
            
            # even length palindromes
            help = self.expand(s, i, i+1)
            if end-start< help[1]-help[0]:
                start = help[0]
                end = help[1]

        return s[start:end+1]          