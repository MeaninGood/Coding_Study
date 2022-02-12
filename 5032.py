a, b, c = map(int, input().split())

temp = (a + b) // c

cnt = 0
while temp > c :
    temp -= c
    cnt += 1
    
print((a+b)//c + cnt)