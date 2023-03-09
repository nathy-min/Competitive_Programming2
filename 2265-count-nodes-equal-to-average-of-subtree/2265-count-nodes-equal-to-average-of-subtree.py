# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subSum(self, node):
        if not node:
            return 0, 0
        ls, lc = self.subSum(node.left)
        rs, rc = self.subSum(node.right)
        
        curr_sum = ls + rs + node.val
        cur_count = lc + rc + 1
        
        if cur_count and node.val == curr_sum // cur_count:
            self.count += 1
        
        return curr_sum, cur_count
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        res_sum, res_count = self.subSum(root)
        
        return self.count