test_case = int(input())
 
for _ in range(test_case):
    n,m = map(int,input().split())
 
    grid = []
    max_count = 0
    add_arr = [0 for _ in range(2 * max(n, m))]
    minus_arr = [0 for _ in range(2 * max(n, m))]
    no_row = 0
    
    for _ in range(n):
        row = list(map(int, input().split()))
        grid.append(row)
        
        for col in range(len(row)):
            add_arr[col + no_row] += row[col] 
            minus_arr[no_row - col] += row[col] 
       
        no_row += 1
        max_sum = 0
    
    for i in range(n):
        for j in range(m):
            temp = add_arr[i + j] + minus_arr[i - j] - grid[i][j]
            max_sum = max(max_sum, temp)
    
    print(max_sum)        
            
                