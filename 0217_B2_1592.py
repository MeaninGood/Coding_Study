# 1592번_영식이와 친구들

## 시계방향으로 1부터 N까지 적혀있는 자리에 앉음
## 일단 1번 자리에 앉은 사람이 공을 받은 후 공을 다른 사람에게 던진다
## 공 던지고 받기 반복,  한 사람이 공을 M번 받았으면 게임은 끝(지금 받은 공도 포함)
## 공을 M번보다 적게 받은 사람이 공을 던질 때,
## 현재 공을 받은 횟수가 홀수번이면 자기의 현재 위치에서 시계 방향으로 L번째 있는 사람에게
## 짝수번이면 자기의 현재 위치에서 반시계 방향으로 L번째 있는 사람에게 공을 던짐
## 공을 총 몇 번 던지는지 구하는 프로그램

'''
# 첫째 줄에 N, M, L
# N은 3보다 크거나 같고, 50보다 작거나 같은 자연수
# M은 50보다 작거나 같은 자연수
# L은 N-1보다 작거나 같은 자연수
## 첫째 줄에 공을 몇 번 던지는지 횟수를 출력

(입력)
5 3 2

(출력)
10

'''
'''
(5 3 2)
1 3 5 2 4 1 4 2 5 3//1


(15 4 9)
1 10 4 13 7 1 7 13 4 10 1 10 4 13 7//1

1. 15 -> 1, 1 -> 15로 가야하므로 %로 연산
2. 범위 잡고 while문 돌리기

'''
n, m, l = map(int, input().split())
arr = [0] * n # 공 받는 횟수 카운트해줄 0으로 생성

cnt = 0 # 공 던지는 횟수 카운트
idx = 0 # arr 배열의 인덱스
while arr[idx] != m-1: # 4번 받으면 3번에서 끊어야 하므로 m-1로 설정
    arr[idx] += 1 # 0번이 무조건 공 받는 걸로 시작
    cnt += 1 # 카운트 +1 
    
    if arr[idx] % 2 : # 홀수면
        idx = (idx + l) % n # 시계 방향
    else : # 짝수면
        idx = (idx - l) % n # 반시계 방향

print(cnt)