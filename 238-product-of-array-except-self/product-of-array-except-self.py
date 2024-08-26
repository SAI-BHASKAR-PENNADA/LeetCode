class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1, nums[0]]
        right = [1, nums[-1]]

        for i in range(2, len(nums)):
            left.append(nums[i-1]*left[-1])
        for i in range(len(nums) - 3, -1, -1):
            right.append(right[-1]*nums[i+1])
        right.reverse()

        ans = []
        for i in range(0, len(left)):
            ans.append(left[i]*right[i])
        return ans