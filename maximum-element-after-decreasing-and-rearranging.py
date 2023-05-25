class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        n = len(arr)
        arr[0] = 1
        for i in range(n - 1):
            if arr[i + 1] - 1 > arr[i]:
                arr[i + 1] = arr[i] + 1

        return max(arr)