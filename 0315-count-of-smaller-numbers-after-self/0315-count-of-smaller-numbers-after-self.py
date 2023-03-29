class Solution:
    def mergeSort(self, left, right, arr):
        if left == right:
            return [arr[right]]
        
        mid = left + (right - left) // 2
        arr1 = self.mergeSort(left, mid, arr)
        arr2 = self.mergeSort(mid + 1, right, arr)
        
        ptr = 0
        for val in arr1:
            while ptr < len(arr2) and val[1] > arr2[ptr][1]:
                ptr += 1
            self.ans[val[0]] += ptr
        
        return self.merger(arr1, arr2)

    def merger(self, arr1, arr2):
        res = []
        ptr1 = ptr2 = 0
        
        while ptr1 < len(arr1) and ptr2 < len(arr2):
            if arr1[ptr1][1] <= arr2[ptr2][1]:
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
    
    def countSmaller(self, nums: List[int]) -> List[int]:
        nums = list(enumerate(nums))
        self.ans = [0 for _ in range(len(nums))]
        
        self.mergeSort(0, len(nums) - 1, nums)
        
        return self.ans