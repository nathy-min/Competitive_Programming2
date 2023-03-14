class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = deque()
        max_arr = []
        
        for i in range(k):
            while que and nums[que[-1]] <= nums[i]:
                que.pop() 
            que.append(i)
            
        max_arr.append(nums[que[0]])
        
        for i in range(k, len(nums)):
            while que and nums[que[-1]] <= nums[i]:
                que.pop() 
            que.append(i)
            
            if que[0] <= i - k:
                que.popleft()
            max_arr.append(nums[que[0]])
        
        return max_arr
            
            