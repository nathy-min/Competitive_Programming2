class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left = 0
        min_q = []
        max_q = []
        max_sub = 0
        
        for right in range(len(nums)):
            val = nums[right]
            
            while min_q and min_q[-1] > val:
                    min_q.pop()
            min_q.append(val)
            
            while max_q and max_q[-1] < val:
                max_q.pop()
            max_q.append(val)
            
            while max_q[0] - min_q[0] > limit:
                if max_q[0] == nums[left]:
                    max_q.pop(0)
                if min_q[0] == nums[left]:
                    min_q.pop(0)
                left += 1
            max_sub = max(max_sub, right - left +  1)    
        return max_sub           