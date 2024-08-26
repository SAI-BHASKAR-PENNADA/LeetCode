class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        vals = {}
        for num in nums:
            if num in vals:
                vals[num] += 1
            else:
                vals[num] = 1
        print(vals)
        pairs = []
        for val in vals:
            pairs.append([vals[val], val])
        pairs.sort(reverse=True)
        print(pairs)
        ans = []
        for pair in pairs:
            if len(ans) == k:
                return ans
            ans.append(pair[1])
        return ans