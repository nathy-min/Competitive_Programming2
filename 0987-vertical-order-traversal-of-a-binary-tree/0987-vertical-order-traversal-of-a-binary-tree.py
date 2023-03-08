# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.dicto = {}
        self.vertical_by_N(root , 0 , 0)

        ele_index = sorted(self.dicto)
        result = []
        for idx in ele_index:
            self.dicto[idx].sort()
            res = []
            for ele in self.dicto[idx]:
                res.append(ele[1])
            result.append(res)

        return result
            

    def vertical_by_N(self , root , x , y) :
        if not root:
            return 

        if  y in self.dicto:
            self.dicto[y].append((x , root.val))

        else:
            self.dicto[y] = [(x , root.val)]
        self.vertical_by_N(root.left, x + 1, y - 1)
        self.vertical_by_N(root.right, x + 1, y + 1)