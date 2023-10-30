# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getleft(self, node):
        cur = node
        while cur.left:
            cur = cur.left
            
        return cur.val   
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            
            temp = self.getleft(root.right)
            root.val = temp
            root.right = self.deleteNode(root.right, temp)
        
        return root