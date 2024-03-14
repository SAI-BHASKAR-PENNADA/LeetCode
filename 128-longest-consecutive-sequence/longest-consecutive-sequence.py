class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:        
        reps = set()
        for num in nums:
            reps.add(num)

        nums = []
        for rep in reps:
            nums.append(rep)

        if len(nums) <= 1:
            return len(nums)

        nums.sort()
        start = 0
        end = 1
        ans = 0
        while end < len(nums):
            if nums[end] != nums[end-1] + 1:
                start = end
                end += 1
            else:
                end += 1

            ans = max(ans, end - start)
        
        return ans
