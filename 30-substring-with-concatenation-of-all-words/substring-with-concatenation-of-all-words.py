class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # return []
        # convert words into a map to check if its there?
        wordMap = {}
        for word in words:
            if word not in wordMap:
                wordMap[word] = 1
            else:
                wordMap[word] += 1
        
        wordLen = len(words[0])
        windowLen = len(words)*wordLen

        start, end = 0, windowLen - 1
        ans = []
        validStrings = set()
        while end < len(s):
            # check current window validity
            if s[start:end+1] in validStrings:
                ans.append(start)
                start += 1
                end += 1
                continue
                
            wordMapCopy = wordMap.copy()
            i = start
            while i <= end:
                if s[i:i+wordLen] not in wordMapCopy or wordMapCopy[s[i:i+wordLen]] == 0:
                    break
                else:
                    wordMapCopy[s[i:i+wordLen]] -= 1
                i = i + wordLen

            if i > end:
                ans.append(start)
                validStrings.add(s[start:end+1])
            start += 1
            end += 1
        return ans
        