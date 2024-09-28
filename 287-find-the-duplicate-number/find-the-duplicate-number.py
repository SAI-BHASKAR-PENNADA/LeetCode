class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        myset = set()
        for num in nums:
            if num in myset:
                return num
            else:
                myset.add(num)