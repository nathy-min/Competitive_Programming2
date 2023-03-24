class Solution:
    def mergesort(self,left, right, arr):
        if left == right:
            return [arr[left]]
        mid = left + (right - left) // 2
        arr1 = self.mergesort(left, mid, arr)
        arr2 = self.mergesort(mid + 1, right, arr)
        
        ptr = 0
        for i in range(len(arr1)):
            if arr1[i] < 2 * arr2[0]:
                continue
            self.count += ptr    
            while ptr < len(arr2) and arr1[i] > 2 * arr2[ptr]:
                self.count += 1
                ptr += 1
        
        return self.merger(arr1, arr2)
    
    def merger(self, arr1, arr2):
        res = []
        ptr1 = ptr2 = 0
        
        while ptr1 != len(arr1) and ptr2 != len(arr2):
            if arr1[ptr1] <= arr2[ptr2]:
                res.append(arr1[ptr1])
                ptr1 += 1
            else:
                res.append(arr2[ptr2])
                ptr2 += 1
        
        if ptr1 != len(arr1):
            res.extend(arr1[ptr1:])
        if ptr2 != len(arr2):
            res.extend(arr2[ptr2:])
        
        return res
    
    def reversePairs(self, nums: List[int]) -> int:
        self.count = 0
        self.mergesort(0, len(nums) - 1, nums)
        
        return self.count
        
        