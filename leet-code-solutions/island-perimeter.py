class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        land = set()
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    if (i - 1, j) in land:
                        perimeter -= 2
                    if (i, j - 1) in land:
                        perimeter -= 2
                    perimeter += 4 
                    land.add((i, j))

        return perimeter                   
