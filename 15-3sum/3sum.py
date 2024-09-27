class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for start in range(0, len(nums) - 2):
            if start != 0 and nums[start] == nums[start - 1]:
                continue 
            i = start + 1
            j = len(nums) - 1
            target = -1 * nums[start]
            while i < j:
                if nums[i] + nums[j] == target:
                    ans.append([nums[start], nums[i], nums[j]])
                    i += 1
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                    j -= 1
                    while j > i and nums[j] == nums[j+1]:
                        j -= 1 
                elif nums[i] + nums[j] < target:
                    i += 1
                else:
                    j -= 1
        return ans