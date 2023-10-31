class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = Counter(nums)
        max_elements = [nums[0]]
        for key, val in count.items():
            if val > count[max_elements[-1]]:
                max_elements = [key]
            elif val == count[max_elements[-1]]:
                max_elements.append(key)

        min_sub = float('inf')
        max_count = count[max_elements[-1]]
        for num in max_elements:
            start = nums.index(num)
            curr = 0
            i = 0
            while curr != max_count:
                if nums[i] == num:
                    curr += 1
                i += 1
            min_sub = min(min_sub, i - start)

        return min_sub            

