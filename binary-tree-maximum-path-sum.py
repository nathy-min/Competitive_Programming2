# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if not node:
            return 0

        left_path = self.dfs(node.left) + node.val
        right_path = self.dfs(node.right) + node.val
        curr_total = left_path + right_path - node.val
        max1 = max(left_path, right_path, node.val)
        self.max_path = max(self.max_path, curr_total, max1)

        return max1

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path = float('-inf')

        self.dfs(root)

        return self.max_path