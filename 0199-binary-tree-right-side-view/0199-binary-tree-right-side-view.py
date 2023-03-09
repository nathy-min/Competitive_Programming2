# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSide(self, node, level):
        if not node:
            return 
        if len(self.ans) == level:
            self.ans.append(node.val)
        self.rightSide(node.right, level + 1)
        self.rightSide(node.left, level + 1)
        
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        
        self.rightSide(root, 0)
        return self.ans