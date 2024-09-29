class Solution:
    def recursion(self, nums, available, current, ans):
        if len(current) == len(nums):
            ans.append(current.copy())
            return 
        
        for num in nums:
            if num in available:
                current.append(num)
                available.remove(num)
                self.recursion(nums, available, current, ans)
                current.pop()
                available.add(num)

    def permute(self, nums: List[int]) -> List[List[int]]:
        available = set(nums)
        ans = []
        self.recursion(nums, available, [], ans)
        return ans