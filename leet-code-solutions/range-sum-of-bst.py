# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            nonlocal total_sum 
            if not node:
                return 
            if low <= node.val <= high:
                total_sum += node.val

            dfs(node.left)
            dfs(node.right)
            
        total_sum = 0
        dfs(root)
        return total_sum    