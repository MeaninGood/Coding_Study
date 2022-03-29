n, m = map(int, input().split())

arr = [int(input()) for i in range(m)] # 색깔별 보석 리스트

arr.sort() # 보석들 정렬해줌

def check(x): # mid의 T, F 체크해줄 함수
    total = 0 # 사람수
    for i in range(len(arr)): # arr 배열을 돌면서
        total += arr[i] // x # 각 보석을 mid로 나눈 몫을 total에 저장 
        
        if arr[i] % x: # 나머지가 있으면
            total += 1 # 1명이 덜 받는다는 뜻이니까 total에 +1 해줌

    return total <= n # total이 총 사람 수인 n명보다 작은지 큰지
                    # True False로 출력
                    # 사람수가 많으면 False 리턴

# 이분탐색
s = 1 # 시작인덱스
e = 10000000000 # 끝인덱스, 충분히 크게 잡아도 됨
idx = 0 # 최종적으로 반환할 idx
while s <= e: # s <= e보다 작을 때
    mid = (s + e) // 2 # 중간값 정해주기
    
    if check(mid): # 중간값으로 나눴을 때의 몫, 나머지의 합이 n보다 작으면
         idx = mid # idx에 mid값 저장
         e = mid - 1 # end는 mid에서 1 빼 줌
         
    else:
        s = mid + 1 # False인 경우 시작 지점을 mid + 1로 해줌

print(idx)