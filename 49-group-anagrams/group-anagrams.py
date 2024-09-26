class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ansMap = {}
        for string in strs:
            key = "".join(sorted(string))
            if key in ansMap:
                ansMap[key].append(string)
            else:
                ansMap[key] = [string]
        ans = []
        for key in ansMap:
            ans.append(ansMap[key])
        return ans