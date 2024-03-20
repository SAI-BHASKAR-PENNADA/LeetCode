class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        print(nums)

        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while (j < k):
                val = nums[i] + nums[j] + nums[k]
                if val < 0:
                    j = j + 1
                elif val > 0:
                    k = k - 1  
                else:
                    helper = [nums[i], nums[j], nums[k]]
                    ans.append(helper)
                    j = j + 1
                    k = k - 1
                    while j < len(nums) - 1 and nums[j] == nums[j - 1]:
                        j = j + 1
                    while k > 0 and nums[k] == nums[k + 1]:
                        k = k - 1
        return ans