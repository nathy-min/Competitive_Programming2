class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        def helper(x_shift, y_shift):
            val = 0
            for i in range(n):
                for j in range(n):
                    if 0 <= i + y_shift < n and 0 <= j + x_shift < n and img1[i + y_shift][j + x_shift] == 1 and img2[i][j] == 1:
                        val += 1
            return val

        lst = []
        for i in range(-n, n):
            for j in range(-n, n):
                lst.append(helper(i, j))

        return max(lst)