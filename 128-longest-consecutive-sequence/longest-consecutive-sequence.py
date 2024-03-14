class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set()

        for num in nums:
            myset.add(num)

        ans = 0
        for num in myset:
            counter = 1
            if num - 1 not in myset:
                num += 1
                while num in myset:
                    num += 1
                    counter += 1
            ans = max(ans, counter)
        
        return ans