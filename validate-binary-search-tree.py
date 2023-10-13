# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            nonlocal ans
            if not node:
                return None, None
            left_min, left_max = dfs(node.left)
            right_min, right_max = dfs(node.right)
            min_val = max_val = node.val

            if left_max or left_max == 0:
                max_val = max(left_max, max_val)
                if node.val <= left_max:
                    ans = False
            if left_min or left_min == 0 :
                min_val = min(min_val, left_min)
                if node.val <= left_min:
                    ans = False
            if right_max or right_max == 0:
                max_val = max(max_val, right_max)
                if node.val >= right_max:
                    ans = False
            if right_min or right_min == 0:
                min_val = min(right_min, min_val)
                if node.val >= right_min:
                    ans = False        

            return min_val, max_val  

        ans = True
        dfs(root)
        return ans