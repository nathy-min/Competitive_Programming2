n, m = map(int, input().split())

grid = [input() for _ in range(n)]

answer = ""

for i in range(n):
    for j in range(m):
        letter = grid[i][j]
        print(grid[i][:j] + grid[i][j+1:])
        row_has_duplicate = letter in grid[i][:j] + grid[i][j+1:]
        col_has_duplicate = letter in [grid[k][j] for k in range(n) if k != i]
        if not row_has_duplicate and not col_has_duplicate:
            answer += letter

print(answer)
