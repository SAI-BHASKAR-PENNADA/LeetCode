class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if len(nums) == 1 or nums[0] < nums[-1]:
        #     return nums[0]

        # for i in range(1, len(nums) - 1):
        #     if nums[i] < nums[i-1] and nums[i] < nums[i+1]:
        #         return nums[i]
        # return nums[-1]

        low = 0
        high = len(nums) - 1

        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return min(nums[0], nums[1])

        while low < high:
            mid = low + (high - low) // 2

            if nums[mid - 1] > nums[mid] and nums[mid + 1] > nums[mid]:
                return nums[mid]
            
            if nums[high] < nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        
        return nums[low]


             

           