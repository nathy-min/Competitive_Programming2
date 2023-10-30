class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        prev_num = 0
        ans = 0
        for num in arr:
            temp = k
            k -= (num - prev_num - 1)
            print(num, k)
            if k <= 0:
                ans = prev_num + temp
                break

            prev_num = num 
        if k > 0:
            ans = prev_num + k
        return ans    