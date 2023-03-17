# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def path(self, root):
        if not root:
            return 0
        curr_sum = 0
        left_sum = self.path(root.left)
        right_sum = self.path(root.right)
        self.max_sum = max(self.max_sum, root.val + left_sum + right_sum)
        cur_max = max(root.val + left_sum, root.val + right_sum, root.val)
        self.max_sum = max(cur_max, self.max_sum)
        
        return cur_max
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        self.path(root)
        
        return self.max_sum