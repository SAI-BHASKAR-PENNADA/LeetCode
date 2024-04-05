class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1:
            return 1

        times = []
        for i in range(len(position)):
            times.append([position[i], ((target - position[i]) / speed[i])])

        times.sort()
        # print(times)
        i = len(times) - 2
        ans = [times[-1][1]]

        while i >= 0:
            if times[i][1] <= ans[-1]:
                i -= 1
            else:
                ans.append(times[i][1])
                i -= 1
    
        return len(ans)

        