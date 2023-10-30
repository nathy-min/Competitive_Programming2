# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node, flag):
            nonlocal ans
            if not node:
                return 0
            left = dfs(node.left, 1)
            right = dfs(node.right, 0)    
            if flag:
                if not (left or right):
                    ans += node.val
            return 1            

        ans = 0
        dfs(root, 0)    
        return ans