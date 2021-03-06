# 10157번_자리배정

## 좌석이 C×R격자형으로 배치
## 가장 왼쪽 아래의 좌석번호는 (1,1)이며, 가장 오른쪽 위 좌석의 번호는 (7,6)
## (1,1)위치 좌석부터 시작
## 시계방향으로 돌아가면서 비어있는 좌석에 관객을 순서대로 배정
## 대기 순서가 K인 관객에게 배정될 좌석 번호 (x,y)를 찾는 프로그램

'''
# 첫 줄에는 공연장의 격자 크기를 나타내는 정수 C와 R, 공백 기준.
# 5 ≤ C, R ≤ 1,000
# 그 다음 줄에는 어떤 관객의 대기번호 K
# 1 ≤ K ≤ 100,000,000
## 두 값, x와 y를 하나의 공백을 사이에 두고 출력
## 좌석을 배정할 수 없는 경우에는 0(숫자 영)을 출력

(입력)
7 6
11

7 6
87

(출력) 
6 6

0

'''

r, c = map(int, input().split())
n = int(input())
arr = [[0]*c for i in range(r)] # c * r의 배열 생성


dx = [0, 1, 0, -1] # 방향 생성
dy = [1, 0, -1, 0] # 오른쪽부터 갈 거니까 dy[0]부터 1로 주고 시작

x = 0 # (0, 0)부터 순회
y = 0
d = 0 # 방향 설정
for i in range(1, r * c + 1): # 숫자는 r*c까지 입력되어야 함
    arr[x][y] = i # arr[0][0]을 1로 놓고 시작
    
    nx = x + dx[d] # 방향 설정, x + dx[d] 초기에는 0인 상태 (오른쪽으로 쭉 가기)
    ny = y + dy[d] # 방향 설정, x + dy[d] 초기에는 0인 상태 (오른쪽으로 쭉 가기)
    # nx, ny가 범위를 벗어났거나 0이 아닌 경우
    if not (0 <= nx < r and 0 <= ny < c) or arr[nx][ny] != 0:
        d = (d + 1) % 4 # 방향 바꿔주기
                        # d+1 % 4 로 해주는 이유는 d + 1 해주면 방향 바뀌지만
                        # 방향이 끝까지 갔을 때 다시 0으로 돌아와야 함
        
    x += dx[d] # x에 방향 좌표대로 값 +-해줌
    y += dy[d] # y에 방향 좌표대로 값 +-해줌

if n > r*c : # n이 범위보다 큰 경우
    print(0) # 0출력

else : # 아니면
    for i in range(r):
        for j in range(c):
            if arr[i][j] == n:
                print(i+1, j+1) # 좌표값 +1씩 해서 출력 0,0부터 시작했기 때문
                exit()