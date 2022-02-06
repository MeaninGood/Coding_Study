# 3985번_롤 케이크

## 길이 L미터의 롤 케이크
## 방청객 N명에게 케이크를 나누어 주려고 함
## 가장 왼쪽 조각이 1번, 오른쪽 조각이 L번 조각
## 방청객은 1번부터 N번까지 번호가 매겨져 있음
## 각 방청객은 종이에 자신이 원하는 조각을 적어서 냄
## 두 수 P와 K를 적어서 내며, P번 조각부터 K번 조각을 원한다는 뜻
## 가장 많은 케이크 조각을 받을 것으로 기대한 방청객의 번호
## 실제로 가장 많은 케이크 조각을 받는 방청객의 번호

'''
# 첫째 줄에 롤 케이크의 길이 L (1 ≤ L ≤ 1000)
# 둘째 줄에는 방청객의 수 N (1 ≤ N ≤ 1000)
# 다음 N개 줄에는 각 방청객 i가 종이에 적어낸 수 Pi와 Ki가 주어짐(1 ≤ Pi ≤ Ki ≤ L, i = 1..N)
## 첫째 줄에 가장 많은 조각을 받을 것으로 기대하고 있던 방청객의 번호를 출력
## 둘째 줄에 실제로 가장 많은 조각을 받은 방청객의 번호를 출력
## 가장 많은 조각을 받도록 예상되는 방청객이 여러 명인 경우에는 번호가 작은 사람을 출력

(입력)
10
5
1 1
1 2
1 3
1 4
7 8

(출력)
4
5

'''

'''
1. 가장 많은 조각을 받을 것으로 기대하고 있던 방청객 번호
: k - p

2. 실제로 가장 많은 조각을 받은 방청객 번호
: 첫사람부터 케이크조각 다 주고 젤 긴 애들!

'''

l = int(input())
n = int(input())

temp = 0
num = 0
for i in range(n) :
    p, k = map(int, input().split())
    
    
    print(temp) 
# print(temp+1)
    
