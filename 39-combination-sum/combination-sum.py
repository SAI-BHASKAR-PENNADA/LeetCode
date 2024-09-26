class Solution:
    def recursion(self, target, candidates, curAns, ans, index):
        if target == 0:
            ans.append(curAns.copy())
            return 
        if index >= len(candidates):
            return
        
        candidate = candidates[index]
        times = 1
        while target >= times*candidate:
            curAns.append(candidate)
            self.recursion(target-times*candidate, candidates, curAns, ans, index+1)
            times += 1
        while times > 1:
            times -= 1
            curAns.pop()
        self.recursion(target, candidates, curAns, ans, index+1)
        

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        curAns = []
        self.recursion(target, candidates, curAns, ans, 0)
        return ans