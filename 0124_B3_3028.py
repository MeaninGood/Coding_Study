


cup = [1, 2, 3]

n = input().upper()

for i in range(len(n)) :
    if n[i] == 'A' :
        cup[0], cup[1] = cup[1], cup[0] # 컵 위치 바꿔주기
        
    elif n[i] == 'B' :
        cup[1], cup[2] = cup[2], cup[1]
        
    else :
        cup[0], cup[2] = cup[2], cup[0]
        
print(cup.index(1)+1) #1의 위치 index로 받아주고, index 0부터 시작하므로 +1 해줌
