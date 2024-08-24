class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(0, len(nums) - 2):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            first = nums[i]

            j = i + 1
            k = len(nums) - 1

            while j < k:
                if first + nums[j] + nums[k] > 0:
                    k -= 1
                elif first + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    ans.append([first, nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < len(nums) and k > j and nums[j] == nums[j-1]:
                        j += 1
                    while k >=0 and k > j and nums[k] == nums[k+1]:
                        k -= 1
        return ans
            

