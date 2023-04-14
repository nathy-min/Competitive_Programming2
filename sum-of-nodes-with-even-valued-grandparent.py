# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, child):
        if not node:
            return
        if child:
            if node.left:
                self.grandchild_sum += node.left.val
            if node.right:
                self.grandchild_sum += node.right.val

        if node.val % 2:
            child = 0
        else:
            child = 1

        self.dfs(node.left, child)
        self.dfs(node.right, child)                    

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.grandchild_sum = 0
        self.dfs(root, 0)

        return self.grandchild_sum