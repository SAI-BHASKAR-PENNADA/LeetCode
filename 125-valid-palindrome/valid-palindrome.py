class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def isAlphaNum(s):
            if s >= 'a' and s <= 'z':
                return True
            if s >= 'A' and s <= 'Z':
                return True
            if s >= '0' and s <= '9':
                return True
            return False
        
        i, j = 0, len(s) - 1

        while i < j:
            if not isAlphaNum(s[i]):
                i += 1
                continue
            if not isAlphaNum(s[j]):
                j -= 1
                continue
            
            if s[i].lower() != s[j].lower():
                return False
            
            i += 1
            j -= 1
        
        return True