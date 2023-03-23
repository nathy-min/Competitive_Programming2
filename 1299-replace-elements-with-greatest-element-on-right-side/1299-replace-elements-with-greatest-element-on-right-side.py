class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_val = arr[len(arr)-1]
        for i in range(len(arr)-1,-1,-1):
            if i == len(arr)-1:
                arr[i] = -1
            else:
                temp = arr[i]
                arr[i] = max_val
                if max_val < temp:
                    max_val = temp
        return arr