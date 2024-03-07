class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)

        ans = []
        while nums:
            first = heapq.heappop(nums)
            second = heapq.heappop(nums)

            ans.append(second)
            ans.append(first)

        return ans