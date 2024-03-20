class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapList = []
        for st in strs:
            dictionary = {}
            for ch in st:
                if dictionary.get(ch) is None:
                    dictionary[ch] = 1
                else:
                    dictionary[ch] = dictionary[ch] + 1 
            mapList.append(dictionary)

        answer = [[strs[0]]]
        # while len(mapList) is not 0:
        #     group = []
        #     placeholder = []
        #     phStrs = []
        #     firstMap = mapList.pop(0)
        #     firstStr = strs.pop(0)
        #     group.append(firstStr)
        #     for i in range(0, len(mapList)):
        #         if len(firstStr) == len(strs[i]) and firstMap == mapList[i]:
        #             group.append(strs[i])
        #         else:
        #             placeholder.append(mapList[i])
        #             phStrs.append(strs[i])
        #     answer.append(group)
        #     mapList = placeholder
        #     strs = phStrs
        maps = [mapList[0]]

        for i in range(1, len(mapList)):
            if mapList[i] not in maps:
                maps.append(mapList[i])
                answer.append([strs[i]])
            else:
                index = maps.index(mapList[i])
                answer[index].append(strs[i])

        return answer