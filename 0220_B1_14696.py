n = int(input())

for i in range(n):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    acnt = [0] * 5
    bcnt = [0] * 5
    
    for i in range(1, a[0]+1):
        acnt[a[i]] += 1

    for i in range(1, b[0]+1):
        bcnt[b[i]] += 1

    for i in range(4, -1, -1):
        if acnt[i] > bcnt[i]:
            print('A')
            break
        
        elif acnt[i] < bcnt[i]:
            print('B')
            break
    else:
        print('D')