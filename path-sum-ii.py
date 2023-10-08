# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def dfs(node, lst):
            nonlocal ans
            nonlocal targetSum
            if not node:
                return
            print(lst, targetSum)    
            lst.append(node.val)
            if not node.left and not node.right:
                if sum(lst) == targetSum:
                    ans.append(lst)
                    return
            temp = lst.copy()
            dfs(node.left, lst)
            dfs(node.right, temp)

        dfs(root, [])
        return ans