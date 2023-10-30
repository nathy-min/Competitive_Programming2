# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        def dfs(node, flag):
            nonlocal ans
            if not node:
                return 
            if node.val in dell:
                dfs(node.left, 1)
                dfs(node.right, 1)
                return 
            if flag:
                ans.append(node)
            node.left = dfs(node.left, 0)
            node.right = dfs(node.right, 0)

            return node            

        ans = []
        dell = set(to_delete)
        dfs(root, 0)
        if root.val not in dell:
            ans.append(root)
        return ans
