class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        sorted_lst = []
        ans = float('inf')

        for i in range(x, len(nums)):
            
            if not sorted_lst:
                sorted_lst.append(nums[i - x])
            
            elif sorted_lst:
                idx = -1
                l, r = 0, len(sorted_lst) - 1
                while l <= r:
                    m = l + (r - l) // 2
                    if sorted_lst[m] <= nums[i - x]:
                        idx = max(idx, m)
                        l = m + 1
                    else:
                        r = m - 1

                sorted_lst.insert(idx + 1, nums[i - x])
            
            
            l, r = 0, len(sorted_lst) - 1
            curr_dif = abs(nums[i] - nums[i - x])  
            while l <= r:
                m = l + (r - l) // 2
                if sorted_lst[m] <= nums[i]:
                    curr_dif = min(curr_dif, abs(sorted_lst[m] - nums[i]))
                    l = m + 1
                else:
                    curr_dif = min(curr_dif, abs(sorted_lst[m] - nums[i]))
                    r = m - 1
            ans = min(ans, curr_dif)  

        return ans          

