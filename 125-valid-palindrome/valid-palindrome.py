class Solution:
    def isalphanum(self, ch):
        if (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z') or (ch >= '0' and ch <= '9'):
            return True
        return False

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i, j = 0, len(s) - 1

        while i < j:
            if not self.isalphanum(s[i]):
                i += 1
            elif not self.isalphanum(s[j]):
                j -= 1
            elif s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True
            