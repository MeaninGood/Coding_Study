# 2864번_5와 6의 차이

## 상근이가 숫자 5를 볼 때, 5로 볼 때도 있지만, 6으로 잘못 볼 수도 있고
## 6을 볼 때는, 6으로 볼 때도 있지만, 5로 잘못 볼 수도 있다
## 두 수 A와 B가 주어졌을 때, 상근이는 이 두 수를 더하려고 한다
## 상근이가 구할 수 있는 두 수의 가능한 합 중, 최솟값과 최댓값을 구해 출력

'''
# 첫째 줄에 두 정수 A와 B가 주어진다. (1 <= A,B <= 1,000,000)
## 첫째 줄에 상근이가 구할 수 있는 두 수의 합 중 최솟값과 최댓값을 출력

(입력)
11 25

1430 4862

(출력)
36 37

6282 6292

''' 

a, b = input().split() 

# 5 -> 6, 6 -> 5 바꿔서 더해주기
min_a = int(a.replace('6', '5'))
min_b = int(b.replace('6', '5'))
max_a = int(a.replace('5', '6'))
max_b = int(b.replace('5', '6'))
            
print(min_a+min_b, max_a+max_b)