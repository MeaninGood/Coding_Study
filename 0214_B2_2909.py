# 2909번_캔디 구매

## 상근이가 지불할 수 있는 가장 가까운 금액으로 사탕의 가격을 반올림
## 상근이가 고른 사탕의 가격이 150원이라면, 사장은 가격을 200원으로 반올림
## 가격이 149원이라면, 사장은 가격을 100원으로 반올림
## 상근이가 가지고 있는 지폐의 액면가는 항상 1, 10, 100, 1000, ..., 1,000,000,000 중 하나
## 지폐 무한개

'''
# 첫째 줄에 사탕의 가격 C와 상근이가 가지고 있는 지폐의 액면가에 적혀있는 0의 개수 K
# (0 ≤ C ≤ 1,000,000,000, 0 ≤ K ≤ 9)
## 첫째 줄에 상근이가 내야하는 가격을 출력

(입력)
184 1

123450995 1

(출력)
180

123451000

'''

c, k = map(int, input().split())

temp = c % 10**k # 짤짤이 계산해 줄 임시 변수 temp 
num = 10**k / 2 # 반올림을 해도 되는지 안 되는지 계산해줄 변수 num
if temp < num: # 짤짤이가 반올림할 값이 아니라면
    print(c-temp) # 그대로 원래 값에서 뺌
    
else : # 반올림 해야 한다면
    print(c- c%10**k + 10**k) # 나머지를 뺴고, 뺀 만큼 10의 k승을 더해줌
