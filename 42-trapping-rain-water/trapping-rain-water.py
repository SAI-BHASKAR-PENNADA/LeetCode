class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax = [-1, height[0]]
        for i in range(2, len(height)):
            leftmax.append(max(leftmax[-1], height[i-1]))
        
        rightmax = [-1, height[-1]]
        for i in range(len(height)-2, -1, -1):
            rightmax.append(max(rightmax[-1], height[i+1]))
        rightmax.reverse()
        
        ans = 0
        for i in range(1, len(height) - 1):
            possible = min(leftmax[i], rightmax[i])
            if possible > height[i]:
                ans += possible - height[i]
        return ans

