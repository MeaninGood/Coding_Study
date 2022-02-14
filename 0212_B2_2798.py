# 2798번_블랙잭

## N장의 카드에 써져 있는 숫자가 주어졌을 때,
## M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력

'''
# 첫째 줄에 카드의 개수 N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000)
# 둘째 줄에는 카드에 쓰여 있는 수가 주어지며, 이 값은 100,000을 넘지 않는 양의 정수
# 합이 M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 입력으로 주어짐
## 첫째 줄에 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력

(입력)
5 21
5 6 7 8 9

(출력)
21

''' 


n, m = map(int, input().split())
cards = list(map(int, input().split()))

li = [] 

# 세 장의 카드 합 그냥 3중 for문으로 구현하기
for i in range(n-2) :
    for j in range(i+1, n-1) :
        for k in range(j+1, n) :
            temp = cards[i]+cards[j]+cards[k]
            if temp > m : # 세 장의 합이 m보다 크면 continue
                continue
            li.append(temp) # 작다면 리스트에 값 추가

print(max(li))