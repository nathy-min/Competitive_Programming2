# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return 'n'
        return str(root.val) + ',' + self.serialize(root.left) + ',' + self.serialize(root.right)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.ptr = 0
        lst = list(data.split(','))
        def dfs():
            if lst[self.ptr] == 'n':
                self.ptr += 1
                return
            node = TreeNode(int(lst[self.ptr]))
            self.ptr += 1
            node.left = dfs() 
            node.right = dfs()

            return node
        return dfs()       
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))