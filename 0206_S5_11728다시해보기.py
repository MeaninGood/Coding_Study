# 11728번_배열 합치기

## 정렬되어있는 두 배열 A와 B
## 두 배열을 합친 다음 정렬해서 출력하는 프로그램을 작성
'''
# 첫째 줄에 배열 A의 크기 N, 배열 B의 크기 M
# 둘째 줄에는 배열 A의 내용이, 셋째 줄에는 배열 B의 내용
# 배열에 들어있는 수는 절댓값이 10**9보다 작거나 같은 정수
## 첫째 줄에 두 배열을 합친 후 정렬한 결과를 출력

(입력)
2 1
4 7
1

(출력)
1 4 7

'''

a, n = map(int, input().split())
#리스트 통쨰로 받기
arr = [list(map(int, input().split())) for i in range(2)] 

# 하나씩 쏙쏙 뽑아서 넣어줄 리스트
result = []

for i in range(a) :
    result.append(arr[0][i])

for j in range(n) :
    result.append(arr[1][j])

result.sort() # 정렬해서
print(*result) # 언패킹 후 프린트

'''
### 이렇게 풀라는 거 아닌 것 같음 ###

메모리 185016 KB
시간 1796ms

'''


