t = int(input())
for _ in range(t):
    num = int(input())
    temp = num
    flag = True
    and_bit = shift =0
    while flag:
        if num % 2 != 0 and not and_bit:
            and_bit = 2**shift
            
        if and_bit:
            flag = False
        num >>= 1
        shift += 1
    
    if temp > and_bit:
        print(and_bit)
    elif temp == 1:
        print(3)
    else:
        print(and_bit + 1)
        
