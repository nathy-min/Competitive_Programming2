class Solution:
    def isDistinct(self, grid):
        # change the grid to a long list then make it in to a set 
        result_set = set(sum(grid, []))
        # check if all are distinct
        if len(result_set) == 9:
            for i in range(1, 10):
                result_set.add(i)

        return len(result_set) == 9

    def is_magic_square(self, grid):
        grid_sum = sum(grid[0])
        if not self.isDistinct(grid):
            return False
        # check rows
        for i in range(3):
            if sum(grid[i]) != grid_sum:
                return False
        # check columns
        for j in range(3):
            if sum(grid[i][j] for i in range(3)) != grid_sum:
                return False
        # check diagonal from top left to bottom right
        if sum(grid[i][i] for i in range(3)) != grid_sum:
            return False
        # check diagonal from top right to bottom left
        if sum(grid[i][2-i] for i in range(3)) != grid_sum:
            return False
        return True

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                subgrid = [[grid[i+k][j+l] for l in range(3)] for k in range(3)]
                if self.is_magic_square(subgrid):
                    count += 1
        return count