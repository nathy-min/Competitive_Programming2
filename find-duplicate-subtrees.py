# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        sub_tree = defaultdict(int)
        def dfs(node):
            if not node:
                return "null"
            s = ','.join([str(node.val), dfs(node.left), dfs(node.right)])
            if sub_tree[s] == 1:
                ans.append(node)
            sub_tree[s] += 1

            return s
        
        ans = []
        dfs(root)
        return ans