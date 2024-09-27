class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        newSet = set(nums)

        ans = 0
        for num in nums:
            count = 1
            crawl = num - 1
            while crawl in newSet:
                count += 1
                newSet.remove(crawl)
                crawl -= 1
            crawl = num + 1
            while crawl in newSet:
                count += 1
                newSet.remove(crawl)
                crawl += 1
            ans = max(ans, count)
        return ans