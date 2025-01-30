class Solution:
    # def convert(self, s: str, numRows: int) -> str:
    #     if numRows == 1:
    #         return s
    #     i, j = 2*(numRows - 1), 0
    #     ans = ''
    #     startIndex = 0
    #     while True:
    #         flip = True
    #         k = startIndex
    #         if k < len(s):
    #             ans += s[k]
    #         while k < len(s):
    #             if flip and i > 0:
    #                 k += i
    #                 if k < len(s):
    #                     ans += s[k]
    #                 else:
    #                     break
    #             elif j > 0:
    #                 k += j
    #                 if k < len(s):
    #                     ans += s[k]
    #                 else:
    #                     break 
    #             flip = not flip
    #         if len(ans) == len(s):
    #             return ans
    #         startIndex += 1
    #         i -= 2
    #         j += 2
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        # The final result string will be built as we go.
        result = []
        
        # Step size, moves down and up in zigzag pattern
        step = 2 * (numRows - 1)
        
        # Iterate over each row
        for row in range(numRows):
            # For each row, we collect characters
            k = row
            while k < len(s):
                result.append(s[k])  # Append the current character
                
                # Determine the next index to move
                # If we're not on the first or last row, there's an "up" jump in the zigzag
                if row != 0 and row != numRows - 1:
                    # Move "up" to the next character in the zigzag
                    up_index = k + step - 2 * row
                    if up_index < len(s):
                        result.append(s[up_index])
                
                # Move down the zigzag to the next character in the vertical
                k += step

        return ''.join(result)


            