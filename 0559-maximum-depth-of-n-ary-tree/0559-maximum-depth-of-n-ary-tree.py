"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def dfs(self, node, lvl):
        ans = lvl
        if not node:
            return 0
        
        for child in node.children:
            ans = max(ans, self.dfs(child, lvl + 1))
       
        return ans

    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        return self.dfs(root, 1)