class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix[0]) - 1
        col = -1
        while l <= r:
            m = (l + r) // 2
            if matrix[0][m] <= target:
                col = max(col, m)
                l = m + 1
            else:
                r = m - 1

        if col == -1:
            return False

        for i in range(col + 1):
            t, b = 0, len(matrix) - 1
            while t <= b:
                m = (t + b) // 2
                if matrix[m][i] == target:
                    return True
                elif matrix[m][i] < target:
                    t = m + 1
                else:
                    b = m - 1

        return False                

