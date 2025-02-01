class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = len(nums) + 1
        start, end = 0, 0
        curSum = nums[end]
        while start <= end:
            if curSum >= target:
                ans = min(ans, end - start + 1)
                curSum -= nums[start]
                start += 1
                
            if curSum < target:
                if end + 1 < len(nums):
                    end += 1
                    curSum += nums[end]
                else:
                    break

        if ans == len(nums) + 1:
            return 0
        return ans