no_v = int(input())
count = 0

for i in range(no_v):
    lst = list(map(int, input().split()))
    count += lst.count(1)
    
print(count // 2)    
    
