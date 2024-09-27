class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        mapsone = {}
        for ch in s1:
            if ch in mapsone:
                mapsone[ch] += 1
            else:
                mapsone[ch] = 1

        for i in range(0, len(s1)):
            if s2[i] in mapsone:
                mapsone[s2[i]] -= 1
            else:
                mapsone[s2[i]] = -1

        numzeros = 0
        for key in mapsone:
            if mapsone[key] == 0:
                numzeros += 1

        # print('before loop ', mapsone, numzeros)

        start = 0
        end = len(s1) - 1
        while end < len(s2):
            if numzeros == len(mapsone):
                return True
              
            if mapsone[s2[start]] == -1:
                numzeros += 1
            if mapsone[s2[start]] == 0:
                numzeros -= 1
            mapsone[s2[start]] += 1

            start = start + 1
            if end + 1 >= len(s2):
                break

            end = end + 1
            if s2[end] in mapsone:
                if mapsone[s2[end]] == 1:
                    numzeros += 1
                if mapsone[s2[end]] == 0:
                    numzeros -= 1
                mapsone[s2[end]] -= 1
            else:
                mapsone[s2[end]] = -1
            # print('in loop ', mapsone, numzeros)
        # print('after loop ', mapsone, numzeros)
        
        return  numzeros == len(mapsone)
            
