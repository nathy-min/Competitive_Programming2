test_case = int(input())

for _ in range(test_case):
    n = int(input())
    a = set(map(int, input().split()))
    a = sorted(list(a))
    len_set = len(a)
    removed = 0
    
    for i in range(len_set - 1):
        if a[i] + 1 == a[i + 1]:
            removed += 1
        else:
            break
    
    if len_set - removed == 1:
        print("YES")
    else:
        print("NO")
        