# 1991번_트리 순회

## 이진 트리를 입력받아 
## 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한 결과를 출력

'''
# 첫째 줄에는 이진 트리의 노드의 개수 N(1 ≤ N ≤ 26)
# 둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어짐
# 노드의 이름은 A부터 차례대로 알파벳 대문자
# 항상 A가 루트 노드가 됨
# 자식 노드가 없는 경우에는 .으로 표현
## 첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 출력
## 각 줄에 N개의 알파벳을 공백 없이 출력

(입력)
7
A B C
B D .
C E F
E . .
F . G
D . .
G . .

(출력)
ABDCEFG
DBAECFG
DBEGFCA

'''

n = int(input())
lft = {}
rgt = {}
for i in range(n):
    a, b, c = map(str, input().split())

    lft[a] = b
    rgt[a] = c

# print(lft)
# print(rgt)
def dfs(cur, option):
    if cur == '.':
        return

    if option == 0:
        print(cur, end='')
    dfs(lft[cur], option)
    if option == 1:
        print(cur, end='')
    dfs(rgt[cur], option)
    if option == 2:
        print(cur, end='')

dfs('A', 0)
print()
dfs('A', 1)
print()
dfs('A', 2)









n = int(input())
lft = {}
rgt = {}
for i in range(n):
    a, b, c = map(str, input().split())

    lft[a] = b
    rgt[a] = c
    
def preorder(cur):
    if cur == '.':
        return
    
    print(cur)
    preorder(lft[cur])
    preorder(rgt[cur])
    
    
def inorder(cur):
    if cur == '.':
        return
    
    inorder(lft[cur])
    print(cur)
    inorder(rgt[cur])
    
    
def postorder(cur):
    if cur == '.':
        return
    
    postorder(lft[cur])
    postorder(rgt[cur])
    print(cur)