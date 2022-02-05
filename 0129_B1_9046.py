# 9046번_복호화

## 알파벳의 빈도수를 체크, 가장 빈번하게 나타나는 문자를 출력
## 가장 빈번하게 나타나는 문자가 여러 개일 경우, '?' 출력
'''
# 첫 째줄 T(1 ≤ T ≤ 20)는 테스트 케이스
# 테스트 케이스는 한 줄마다 소문자와 공백으로 이루어진 영어 문장
## 가장 빈번하게 나타나는 문자를 출력
## 빈번하게 나타나는 문자가 여러 개일 경우 '?'를 출력

(입력)
3
asvdge ef ofmdofn
xvssc kxvbv
hull full suua pmlu

(출력)
f
v
?

'''


'''
1. 각 알파벳의 개수를 카운트해 줄 딕셔너리 생성

xvssc kxvbv 일 때

dic = {}

if alpha not in alpha_dict:
alpha_dict[alpha] = 1

(1) x가 없으므로 dic = { 'x' : 1 }
(2) v가 없으므로 dic = { 'x' : 1, 'v' : 1 }
(3) s가 없으므로 dic = { 'x' : 1, 'v' : 1, 's' : 1 }


else: # 딕셔너리에 알파벳이 있으면
alpha_dict[alpha] += 1 # 해당 알파벳의 value를 2로 바꿔줌

위에 s가 이미 있으니, xvssc kxvbv에서 두 번째 s는 value로 카운트해줌

dic = { 'x' : 1, 'v' : 1, 's' : 2 }

위와 같은 과정을 반복하면 최종적으로

dic = 
{ 'x' : 2, 'v' : 3, 's' : 2, 'c' : 1, 'k' : 1, 'b' : 1 }


2. 카운트한 알파벳 중 최대값만 뽑아줄 변수와 리스트 생성

 hull full suua pmlu의 경우
 u = 5개, l = 5개 이므로
 
 max_val = 5
 maxli = [u, l]

'''


for _ in range(int(input())): # 테스트 케이스로 바로 for문 생성
    data = input()
    alpha_dict = {}  # 내부적으로 딕셔너리 생성
    
    for alpha in data: # 입력받은 문자열을 돌면서
        if alpha == ' ': # 공백일 때는 그대로 continue
            continue
        if alpha not in alpha_dict: # 딕셔너리에 알파벳이 없으면
            alpha_dict[alpha] = 1 # 알파벳을 키로, value는 1로 생성
        else: # 딕셔너리에 알파벳이 있으면
            alpha_dict[alpha] += 1 # 해당 알파벳의 value를 +1 해 줌
    
    # 다음으로 딕셔너리의 value로 바로 접근하여 최대 값을 지정            
    max_val = max(alpha_dict.values())
    # 맥스값들 저장해줄 리스트 (여러 개일 수도 있기 때문에) 
    maxli = []
    
    for alpha, cnt in alpha_dict.items(): # 딕셔너리의 key와 value를 차례로 돌면서
        if cnt == max_val: # value가 맥스 값과 같으면
            maxli.append(alpha) # 리스트에 추가해줌
            
    if len(maxli) == 1: # maxli 리스트에 하나만 있다면 
        print(maxli[0]) # 바로 출력
    else: # 하나가 아니라 여러 개인 경우
        print("?") # 물음표 출력
