# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count = defaultdict(int)
        maxCount = 0

        def traverse(tree):
            nonlocal maxCount

            if not tree:
                return

            val = tree.val
            count[val] += 1
            maxCount = max(maxCount, count[val])

            traverse(tree.left)
            traverse(tree.right)

        traverse(root)

        answer = []

        for num in count:
            if count[num] == maxCount:
                answer.append(num)

        return answer
        
        
        