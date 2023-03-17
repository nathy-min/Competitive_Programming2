# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, curr_sum):
        if not root:
            self.dic[0] += 1
            return 0       
        curr_sum += root.val
        
        
        
        if self.dic[curr_sum - self.target]:
            self.no_path += self.dic[curr_sum - self.target] 
        self.dic[curr_sum] += 1
        
        left_sum = self.helper(root.left, curr_sum)
        self.dic[left_sum] -= 1
        right_sum = self.helper(root.right, curr_sum)
        self.dic[right_sum] -= 1
        
        return curr_sum
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.target = targetSum
        self.dic = defaultdict(int)
        self.dic[0] = 1
        self.no_path = 0
        
        self.helper(root, 0)
        
        return self.no_path