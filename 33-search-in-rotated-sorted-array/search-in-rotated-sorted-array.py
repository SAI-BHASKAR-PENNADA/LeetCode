class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = low + (high - low) // 2
            if low == high - 1:
                break
            if nums[mid] == target:
                return mid
            if nums[low] < nums[mid]:
                # left part is sorted
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            if nums[mid] < nums[high]:
                # right part is sorted
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        
        if low == high:
            return low if nums[low] == target else -1
        if low == high - 1:
            if nums[low] == target:
                return low
            if nums[high] == target:
                return high
        return -1 