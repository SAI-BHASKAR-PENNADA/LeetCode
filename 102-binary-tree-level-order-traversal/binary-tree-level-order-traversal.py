# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [root, None]
        ans = []
        stage = []
        while queue:
            pointer = queue.pop(0)
            if not pointer:
                if stage:
                    ans.append(stage)
                stage = []
                if queue:
                    queue.append(None)
            else:
                stage.append(pointer.val)
                if pointer.left:
                    queue.append(pointer.left)
                if pointer.right:
                    queue.append(pointer.right)
        return ans



