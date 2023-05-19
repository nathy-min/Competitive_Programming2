class Solution:
    def find(self, x, y):
        if (x, y) != self.root[x][y]:
            self.root[x][y] = self.find(self.root[x][y][0], self.root[x][y][1])
            
        return self.root[x][y]
    def union(self, curr, right, bottom):
        curr_pa = self.find(curr[0], curr[1])
        temp = curr_pa
        right_pa = self.find(right[0], right[1])
        bottom_pa = self.find(bottom[0], bottom[1])

        if right[0] != -1:
            if self.grid[curr[0]][curr[1]] in self.left and self.grid[right[0]][right[1]] in self.right:
                if self.rank[right_pa[0]][right_pa[1]] > self.rank[curr_pa[0]][curr_pa[1]]:
                    curr_pa, right_pa = right_pa, curr_pa
                self.root[right_pa[0]][right_pa[1]] = curr_pa
                self.rank[curr_pa[0]][curr_pa[1]] += self.rank[right_pa[0]][right_pa[1]]    
        if bottom[0] != -1:
            if self.grid[curr[0]][curr[1]] in self.up and self.grid[bottom[0]][bottom[1]] in self.bottom:
                if self.rank[bottom_pa[0]][bottom_pa[1]] > self.rank[temp[0]][temp[1]]:
                    temp, bottom_pa = bottom_pa, temp
                self.root[bottom_pa[0]][bottom_pa[1]] = temp
                self.rank[temp[0]][temp[1]] += self.rank[bottom_pa[0]][bottom_pa[1]]

    def hasValidPath(self, grid: List[List[int]]) -> bool:
        self.grid = grid
        self.root = []
        self.rank = []
        self.up = {2, 3, 4}
        self.bottom = {2, 5, 6}
        self.left = {1, 4, 6}
        self.right = {1, 3, 5}

        for i in range(len(grid)):
            row = []
            for j in range(len(grid[0])):
                row.append((i, j))
            self.root.append(row)    
            self.rank.append([1] * len(grid[0]))
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                right, bottom = (-1, 0), (-1, 0)
                if j + 1 < len(grid[0]):
                    right = (i, j + 1)
                if i + 1 < len(grid):
                    bottom = (i + 1, j)
                self.union((i, j), right, bottom) 
                   
        return self.find(0, 0) == self.find(len(grid) - 1, len(grid[0]) - 1)