# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, visited):
        if not node:
            return 
        if not node.left and not node.right:
            visited += str(node.val)
            self.total += int(visited)
            return
        
        visited += str(node.val)
        self.dfs(node.left, visited)
        self.dfs(node.right, visited)
        
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        
        self.dfs(root, "")
        
        return self.total