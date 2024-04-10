class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax = [0]

        for i in range(1, len(height)):
            leftmax.append(max(height[i-1], leftmax[i-1]))
        
        rightmax = [0]

        for i in range(len(height) - 2, -1, -1):
            rightmax.append(max(height[i+1], rightmax[-1]))
        
        rightmax.reverse()

        ans = 0

        for i in range(len(leftmax)):
            if min(leftmax[i], rightmax[i]) - height[i] > 0:
                ans += min(leftmax[i], rightmax[i]) - height[i]
        return ans