class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mymap = {}
        for string in strs:
            sortedString = "".join(sorted(string))
            # print(sortedString)
            if sortedString in mymap:
                mymap[sortedString].append(string)
            else:
                mymap[sortedString] = [string]
        
        ans = []
        for maps in mymap:
            ans.append(mymap[maps])
        return ans