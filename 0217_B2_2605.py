# 2605번_줄 세우기

## 학생들이 한 줄로 줄을 선 후, 첫 번째 학생부터 차례로 번호를 뽑는다 
## 첫 번째로 줄을 선 학생은 무조건 0번 번호를 받아 제일 앞에 줄을 선다
## 두 번째로 줄을 선 학생은 0번 또는 1번 둘 중 하나의 번호를 뽑는다
## 0번을 뽑으면 그 자리에 그대로 있고, 1번을 뽑으면 바로 앞의 학생 앞으로 가서 줄을 선다
## 세번째로 줄을 선 학생은 0, 1 또는 2 중 하나의 번호를 뽑는다
## 뽑은 번호만큼 앞자리로 가서 줄을 선다
'''
예를 들어 5명의 학생이 줄을 서고,
첫 번째로 줄을 선 학생부터 다섯 번째로 줄을 선 학생까지 
차례로 0, 1, 1, 3, 2번의 번호를 뽑았다면

첫 번째 학생부터 다섯 번째 학생까지 1부터 5로 표시하면 
학생들이 줄을 선 순서는 다음과 같이 된다.

첫 번째 학생이 번호를 뽑은 후 : 1
두 번째 학생이 번호를 뽑은 후 : 2 1
세 번째 학생이 번호를 뽑은 후 : 2 3 1
네 번째 학생이 번호를 뽑은 후 : 4 2 3 1
다섯 번째 학생이 번호를 뽑은 후 : 4 2 5 3 1

'''

'''
# 첫째 줄에는 학생의 수
#  둘째 줄에는 줄을 선 차례대로 학생들이 뽑은 번호가 주어짐
# 학생의 수가 100 이하이고,
# 학생들이 뽑는 번호는 0 또는 자연수이며 학생들이 뽑은 번호 사이에는 빈 칸이 하나씩
## 첫째 줄에 학생들이 최종적으로 줄을 선 순서를 그 번호로 공백을 두고 출력

(입력)
5
0 1 1 3 2

(출력)
4 2 5 3 1

'''


'''
1 2 3 4 5
0, 1, 1, 3, 2
# i - 리스트[i]로 삽입
1
2 1
2 3 1
4 2 3 1
4 2 5 3 1

'''

n = int(input())
li = list(map(int, input().split()))

arr = []
for i in range(n): # range(1~6)
    arr.insert(i-li[i], i+1) # 0-0, 1-1, 2-1, 3-3, 4-2로 가야 함
    
print(*arr)
    