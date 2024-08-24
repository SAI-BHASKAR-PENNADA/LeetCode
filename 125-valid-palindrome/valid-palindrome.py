class Solution:
    def isalphanum(self, ch):
        if (ch >= 65 and ch <= 90) or (ch >= 97 and ch <= 122) or (ch >= 48 and ch <= 57):
            return True
        return False

    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        while i < j:
            if not self.isalphanum(ord(s[i])):
                i += 1
            elif not self.isalphanum(ord(s[j])):
                j -= 1
            elif s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
        return True
            