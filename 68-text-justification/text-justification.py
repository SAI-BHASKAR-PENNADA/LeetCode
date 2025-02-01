class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        i = 0
        while i < len(words):
            curLen = len(words[i])
            start = i + 1
            while start < len(words) and maxWidth >= curLen + 1 + len(words[start]):
                curLen += 1 + len(words[start])
                start += 1

            # construct current string
            spaces = maxWidth - curLen
            nWords = start - i
            additionalSpaces = 0
            if start < len(words) and nWords > 1:
                additionalSpaces = spaces // (nWords - 1)
            leftJustSpaces = 0
            if start < len(words) and nWords > 1:
                leftJustSpaces = spaces % (nWords - 1)
            print(spaces, nWords, additionalSpaces, leftJustSpaces)
            string = words[i]
            for j in range(i+1, start):
                nSpaces = 1 + additionalSpaces
                if leftJustSpaces > 0:
                    nSpaces += 1
                    leftJustSpaces -= 1
                string += " "*(nSpaces) + words[j]
            
            # if start >= len(words):
            string += " "*(maxWidth - len(string)) 
            ans.append(string)
            i = start
        return ans