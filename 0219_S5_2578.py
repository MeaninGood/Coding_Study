# 2578번_빙고

## 25개의 칸으로 이루어진 빙고판에 1부터 25까지 자연수를 한 칸에 하나씩 
## 사회자가 부르는 수를 차례로 지워나갸면서
## 선이 3줄 이상일 때 빙고
## 사회자가 몇 번째 수를 부른 후 철수가 "빙고"를 외치게 되는지를 출력

'''
# 1~5줄까지 빙고판에 쓰여진 수가 차례대로 한 줄에 다섯 개씩 공백 기준으로 주어짐
# 열째 줄까지 지울 숫자가 차례대로 한 줄에 다섯 개씩 빈 칸을 사이에 두고 주어짐
## 첫째 줄에 사회자가 몇 번째 수를 부른 후 철수가 "빙고"를 외치게 되는지 출력

(입력)
11 12 2 24 10
16 1 13 3 25
6 20 5 21 17
19 4 8 14 9
22 15 7 23 18
5 10 7 16 2
4 22 8 17 13
3 18 1 6 25
12 19 23 14 21
11 24 9 20 15

(출력)
15

'''
'''
11 12 0 24 0
0 1 13 3 25
6 20 0 21 17
19 4 8 14 9
22 15 0 23 18
'''
'''
5 10 7 16 2
4 22 8 17 13
3 18 1 6 25
12 19 23 14 21
11 24 9 20 15
'''

arr = [list(map(int, input().split())) for i in range(5)]
nums = [list(map(int, input().split())) for i in range(5)]

def erase(x):
    for i in range(5):
        for j in range(5):
            if arr[i][j] == x:
                arr[i][j] = 0

def is_bingo():
    ret = 0
    for i in range(5):
        cnt = 0
        for j in range(5):
            if arr[i][j] == 0:
                cnt += 1
                
        if cnt == 5:
            ret += 1
        
        cnt = 0
        for j in range(5):
            if arr[j][i] == 0:
                cnt += 1
                
        if cnt == 5:
            ret += 1
                
    cnt = 0 
    for i in range(5):
        if arr[i][i] == 0:
            cnt += 1
            
    if cnt == 5:
        ret += 1
        
    cnt = 0
    for i in range(5):
        if arr[i][4 - i] == 0:
            cnt += 1
            
    if cnt == 5:
        ret += 1
    
    return ret >= 3 # ret이 이상인지 아닌지 T, F Return

cnt = 0
for i in range(5):
    for j in range(5):
        cnt += 1
        # 1. nums의 숫자를 arr에서 찾아서 지우기
        erase(nums[i][j])
        # 2. 빙고가 되는지 확인하기
        if is_bingo():
            print(cnt)
            exit()
        # 3. 몇 번째로 부른 숫자인지 출력 후 종료