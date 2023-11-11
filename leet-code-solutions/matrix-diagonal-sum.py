class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total_sum = 0
        n = len(mat)
        for i in range(n):
            total_sum += mat[i][i] + mat[i][n - i - 1]

        half = n // 2
        if n % 2:
            return total_sum - mat[half][half]
        else:
            return total_sum        