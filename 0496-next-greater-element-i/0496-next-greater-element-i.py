class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_map = defaultdict(int)
        d_stack = []
        for i in range(len(nums2)):
            if d_stack:
                while d_stack and d_stack[-1] < nums2[i]:
                    num_map[d_stack.pop()] = nums2[i]
                d_stack.append(nums2[i])    
            else:
                d_stack.append(nums2[i])
        for i in range(len(nums1)):
            val = num_map[nums1[i]]
            if val:
                nums1[i] = val
            else:
                nums1[i] = -1
        return nums1