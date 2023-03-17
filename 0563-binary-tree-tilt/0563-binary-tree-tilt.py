# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tilt(self, root):
        if not root:
            return 0
        left_sum = self.tilt(root.left)
        right_sum = self.tilt(root.right)
        self.tilt_sum += abs(left_sum - right_sum)
        
        return root.val + left_sum + right_sum
    
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.tilt_sum = 0
        self.tilt(root)
        
        return self.tilt_sum