class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            if not stack or stack[-1][0] >= temperatures[i]:
                stack.append([temperatures[i], i])
            else:
                while stack and stack[-1][0] < temperatures[i]:
                    ans[stack[-1][1]] = i - stack[-1][1]
                    stack.pop()
                stack.append([temperatures[i], i])
        
        return ans










# 74, 1
# 73, 0

# 1, 0, 0, 0, 0, 0, 0, 0