# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root, ans):
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1
        
        leftheight = self.height(root.left, ans)
        rightheight = self.height(root.right, ans)
        
        if abs(leftheight-rightheight) > 1:
            ans[0] = False
        return max(leftheight, rightheight) + 1
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = [True]
        self.height(root, ans)
        return ans[0]