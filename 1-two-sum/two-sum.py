class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n^2)
        # for i in range(0, len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # O(n)
        store = {}
        for i in range(0, len(nums)):
            lookfor = target - nums[i]
            if lookfor in store:
                return [i, store[lookfor]]
            store[nums[i]] = i

