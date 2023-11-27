# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        arr = []
        def dfs(node):
            if not(node):
                return 
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)

        dfs(root)
        root = curr = TreeNode(arr[0])
        for i in arr[1:]:
            curr.right = TreeNode(i)
            curr = curr.right
        return root