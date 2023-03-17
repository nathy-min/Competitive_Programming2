# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node, low, high ):
        if not node:
            return True

        val = node.val
        if val <= low or val >= high:
            return False

        return self.helper(node.left, low, val) and self.helper(node.right, val, high)
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, float('-inf'), float('inf'))