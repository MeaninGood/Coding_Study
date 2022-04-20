# 1946번_신입 사원

## 어떤 지원자 A의 성적이 다른 어떤 지원자 B의 성적에 비해 
## 서류 심사 결과와 면접 성적이 모두 떨어진다면 A는 결코 선발되지 않음
## 선발할 수 있는 신입사원의 최대 인원수를 구하기

'''
# 첫째 줄에는 테스트 케이스의 개수 T(1 ≤ T ≤ 20)
# 각 테스트 케이스의 첫째 줄에 지원자의 숫자 N(1 ≤ N ≤ 100,000)
# 둘째 줄부터 N개 줄에는 각각의 지원자의 서류심사 성적, 면접 성적의 순위가 공백을 사이에 두고 한 줄에 주어짐
# 두 성적 순위는 모두 1위부터 N위까지 동석차 없이 결정됨
## 각 테스트 케이스에 대해서 진영 주식회사가 선발할 수 있는 신입사원의 최대 인원수를 한 줄에 하나씩 출력

(입력)
2
5
3 2
1 4
4 1
2 3
5 5
7
3 6
7 3
4 2
1 4
5 7
2 5
6 1

(출력) 
4
3

'''

T = int(input())

for tc in range(T):
    n = int(input())
    v = [list(map(int, input().split())) for _ in range(n)]

    v.sort(key = lambda x: x[0])

    idx = v[0][1]
    cnt = 1
    for i in range(1, n):        
        if v[i][1] < idx:
            idx = v[i][1]
            cnt += 1
        
    print(cnt)
    
    
'''
1
5
1 1
2 5
3 4
4 3
5 2
'''