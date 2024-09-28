class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = []
        for i in range(len(temperatures) - 1, -1, -1):
            if not stack:
                stack.append([temperatures[i], i])
                ans.append(0)
            else:
                if temperatures[i] < stack[-1][0]:
                    ans.append(stack[-1][1] - i)
                    stack.append([temperatures[i], i])
                else:
                    while stack and stack[-1][0] <= temperatures[i]:
                        stack.pop()
                    if not stack:
                        stack.append([temperatures[i], i])
                        ans.append(0)
                    else:
                        ans.append(stack[-1][1] - i)
                        stack.append([temperatures[i], i])
                        
        ans.reverse()
        return ans