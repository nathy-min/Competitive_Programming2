# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        def dfs(node):
            
            if not node:
                return 
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                dfs(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                dfs(node.right)

        res = []
        visited = set()
        
        def find(node, count):
            if count == k:
                res.append(node)
                print(res)
                return
            visited.add(node)    
            for nei in graph[node]:
                print(nei)
                if nei not in visited:
                    find(nei, count + 1)

        dfs(root) 
            
        find(target.val, 0)
        return res       
