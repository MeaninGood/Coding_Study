# 13420번_사칙연산

## 사칙연산을 이용한 문제와 답이 주어졌을 때, 올바른 수식인지 계산하여 채첨하는 프로그램

'''
# 첫째 줄에 테스트 케이스 개수 T
# 각 테스트케이스의 첫번째 줄에 수식이 주어짐, 문자와 기호가 공백으로 구분됨
# 사칙연산 기호는 1개만 사용됨, 나눗셈의 경우 항상 나누어떨어지는 경우로만 주어짐
## 각 테스트 케이스의 답을 순서대로 1줄에 1개씩 출력
## 주어진 수식이 정답일 경우 "correct", 오답일 경우 "wrong answer" 출력

(입력)
4
3 * 2 = 6
11 + 11 = 11
7 - 9 = -2
3 * 0 = 0

(출력)
correct
wrong answer
correct
correct

'''

T = int(input())


for i in range(T) :
    num1, idx, num2, eql, temp  = input().split()
    print(temp)
    if str(idx) == '+' :
        result = int(num1) + int(num2)

    elif str(idx) == '-' :
        result = int(num1) - int(num2)

    elif str(idx) == '*' :
        result = int(num1) * int(num2)

    elif str(idx) == '/' :
        result = int(num1) / int(num2)
    
    
    print('correct' if temp == result else 'wrong answer')