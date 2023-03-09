# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []

        def traverse(tree, level):
            if not tree:
                return

            if len(answer) < level:
                answer.append([tree.val])
            else:
                answer[level-1].append(tree.val)

            traverse(tree.left, level + 1)
            traverse(tree.right, level + 1)

        traverse(root, 1)

        return answer