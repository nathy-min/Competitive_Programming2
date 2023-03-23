class Solution:
    def quick_sort(self , left , right , arr , k):
        # if k == :
        #     return arr[k]

        write = left + 1
        read = left + 1
        while read <= right:
            if arr[read] < arr[left]:
                arr[read] , arr[write] = arr[write] , arr[read]
                write += 1

            read += 1

        arr[write - 1] , arr[left] = arr[left] , arr[write - 1]
        if write - 1 == k:
            return arr[write - 1]
        
        elif k < write - 1:
            
            return self.quick_sort(left , write - 2 , arr , k)
        else:
            
            return self.quick_sort(write , right , arr , k)
        
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quick_sort(0 , len(nums) - 1 , nums ,len(nums) - k )
        
        
        