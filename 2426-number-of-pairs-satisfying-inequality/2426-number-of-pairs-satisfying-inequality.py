class Solution:
    def mergesort(self, left, right, arr):
        if left == right:
            return [arr[left]]
        
        mid = left + (right - left) // 2
        arr1 = self.mergesort(left, mid, arr)
        arr2 = self.mergesort(mid + 1, right, arr)

        ptr = 0
        for val in arr2:
            flag = False
            for i in range(ptr, len(arr1)):
                if arr1[i] > (val + self.diff):
                    break
                ptr = i 
                flag = True
            if flag:
                self.count += (ptr + 1)
        
        return self.merger(arr1, arr2)
    
    def merger(self, arr1, arr2):
        ptr1 = ptr2 = 0
        res = []
        
        while ptr1 < len(arr1) and ptr2 < len(arr2):
            if arr1[ptr1] <= arr2[ptr2]:
                res.append(arr1[ptr1])
                ptr1 += 1
            else:
                res.append(arr2[ptr2])
                ptr2 += 1
        
        if ptr1 < len(arr1):
            res.extend(arr1[ptr1:])
        if ptr2 < len(arr2):
            res.extend(arr2[ptr2:])
            
        return res
        
        
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        nums3 = []
        self.diff = diff
        self.count = 0
        
        for i in range(len(nums1)):
            nums3.append(nums1[i] - nums2[i])
        
        self.mergesort(0, len(nums1) - 1, nums3)
        
        return self.count
            
            