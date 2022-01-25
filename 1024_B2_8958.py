N = int(input())

for _ in range(N) :
    result = list(input())
    
    count = 0
    score = 0
    for i in result :
        if i == 'O' :
            count += 1
            score += count
        
        else :
            count = 0
        
    print(score)