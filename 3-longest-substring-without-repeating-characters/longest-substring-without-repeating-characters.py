class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        start, end = 0, 1
        elems = set()
        elems.add(s[start])
        ans = 1
        while end < len(s):
            # print(elems)
            ans = max(ans, end-start)
            if s[end] not in elems:
                elems.add(s[end])
                end += 1
            else:
                elems.remove(s[start])
                start += 1
            
        return max(ans, end-start)