class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort(reverse = True)
        pref_arr = [0 for i in range(len(nums))]
        max_sum = 0
        print(nums)
        for i in range(len(requests)):
            pref_arr[requests[i][0]] += 1
            if requests[i][1] < len(nums) - 1:
                pref_arr[requests[i][1] + 1] -= 1
        
        for i in range(1, len(pref_arr)):
            pref_arr[i] += pref_arr[i - 1]
        
        pref_arr.sort(reverse = True)
        for i in range(len(pref_arr)):
            max_sum += (nums[i] * pref_arr[i])
        
        return max_sum % (10**9 + 7)
            
            
            