# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lst = [p, q]
        ans = ''
        def dfs(node):
            nonlocal ans
            if not node:
                return False
            left = dfs(node.left)
            right = dfs(node.right)
            if ((node in lst) and (left or right)) or (left and right):
                if not ans:
                    print('jfk')
                    ans = node 
                return True 
            elif left or right or node in lst:
                return True
            return False
        
        dfs(root)
        return ans