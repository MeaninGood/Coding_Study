

import math

n = int(input())

score = []
for i in range(n) :
    num = input()
    
    if num == '100' :
        score.append(num)
        
    else :
        tmp = ''
        for j in range(len(num)) :
            if (num[j] == '0') or (num[j] == '6') :
                tmp += '9'
            else :
                tmp += num[j]
            
        score.append(tmp)
        
total = sum(map(int, score))
result = total / n

if result - int(result) >= 0.5 :
    print(math.ceil(result))
else : 
    print(math.floor(result))
