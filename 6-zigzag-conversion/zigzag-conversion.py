class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        i, j = 2*(numRows - 1), 0
        ans = ''
        startIndex = 0
        while True:
            flip = True
            k = startIndex
            if k < len(s):
                ans += s[k]
            while k < len(s):
                if flip and i > 0:
                    k += i
                    if k < len(s):
                        ans += s[k]
                    else:
                        break
                elif j > 0:
                    k += j
                    if k < len(s):
                        ans += s[k]
                    else:
                        break 
                flip = not flip
            if len(ans) == len(s):
                return ans
            startIndex += 1
            i -= 2
            j += 2

            