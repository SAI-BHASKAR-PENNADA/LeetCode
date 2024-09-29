class Solution:
    def rec(self, candidates, curIndex, target, current, ans):
        if target == 0:
            ans.append(current.copy())
            return
        if curIndex == len(candidates):
            return
        
        # add 
        if candidates[curIndex] <= target:
            current.append(candidates[curIndex])
            self.rec(candidates, curIndex+1, target-candidates[curIndex], current, ans)
            current.pop()

        # do not add
        updatedIndex = curIndex + 1
        while updatedIndex < len(candidates) and candidates[updatedIndex] == candidates[updatedIndex - 1]:
            updatedIndex += 1
        self.rec(candidates, updatedIndex, target, current, ans)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        self.rec(candidates, 0, target, [], ans)
        return ans