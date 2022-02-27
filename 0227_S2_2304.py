# 2304번_창고 다각형

## N 개의 막대 기둥이 일렬로 세워져 있음
## 1. 지붕은 수평 부분과 수직 부분으로 구성되며, 모두 연결
## 2. 지붕의 수평 부분은 반드시 어떤 기둥의 윗면과 닿아야 함
## 3. 지붕의 수직 부분은 반드시 어떤 기둥의 옆면과 닿아야 함
## 4. 지붕의 가장자리는 땅에 닿아야 함
## 5. 지붕의 어떤 부분도 오목하게 들어간 부분이 없어야 함
## 기둥들의 위치와 높이가 주어질 때, 가장 작은 창고 다각형의 면적을 구하기


'''
# 첫 줄에는 기둥의 개수를 나타내는 정수 N, N은 1 이상 1,000 이하
# 그 다음 N 개의 줄에는
# 각 기둥의 왼쪽 면의 위치를 나타내는 정수 L
# 높이를 나타내는 정수 H가 한 개의 빈 칸을 사이에 두고 주어짐
# L과 H는 둘 다 1 이상 1,000 이하
## 첫 줄에 창고 다각형의 면적을 나타내는 정수를 출력


(입력)
10 2
3 -2 -4 -9 0 3 7 13 8 -3

(출력) 
21

'''

n = int(input())
# arr[i] : i번 위치에 있는 기둥의 높이. 이 위치에 기둥이 없으면 0
arr = [0 for i in range(1010)]
for i in range(n):
    a, b = map(int, input().split())

    arr[a] = b


# 0~i 중 가장 높은 기둥의 높이를 left[i]에 저장.
left = [0 for i in range(1010)]
left[0] = arr[0]
for i in range(1, 1010):
    left[i] = max(left[i - 1], arr[i])
print(left)

# i~1010중 가장 높은 기둥의 높이를 right[i]에 저장.
right = [0 for i in range(1010)]
for i in range(1009)[::-1]:
    right[i] = max(right[i + 1], arr[i])
print(right)


# i번 위치의 건물 높이는 left[i], right[i]중 작은 값.
ans = 0
for i in range(1010):
    ans += min(left[i], right[i])

print(ans)
