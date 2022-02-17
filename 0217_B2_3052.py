# 3052번_나머지

## 두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 
## 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다
## 그 다음 서로 다른 값이 몇 개 있는지 출력

'''
# 첫째 줄부터 열번째 줄 까지 숫자가 한 줄에 하나씩
# 이 숫자는 1,000보다 작거나 같고, 음이 아닌 정수
## 첫째 줄에, 42로 나누었을 때, 서로 다른 나머지가 몇 개 있는지 출력

(입력)
42
84
252
420
840
126
42
84
420
126

(출력)
1

'''

arr = []
for i in range(10):
    n = int(input())%42 # 바로 42로 나눈 나머지로 값 받기
    arr.append(n) # arr에 추가
    
print(len(set(arr))) # set으로 중복 제거