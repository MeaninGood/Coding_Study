# 2954번_창영이의 일기장

## 모음 a,e,i,o,u 다음에 p를 하나 더 쓰고 그 모음을 하나 더 씀
## 작성한 문장이 주어졌을 때, 원래 문장은 무엇인지 출력

'''
# 첫째 줄에 알파벳 소문자와 공백으로만 이루어진 문장이 하나 주어짐
# 모든 단어는 공백 하나로 구분
# 문장의 길이는 최대 100
## 첫째 줄에 창영이가 일기장에 작성한 문장을 원래 문장으로 바꾸어 출력

(입력)
zepelepenapa papapripikapa

(출력)
zelena paprika

'''



m = input()

li = ['apa', 'epe', 'ipi', 'opo', 'upu']
      
for i in li : # li 리스트에 각각의 모음set 만들어 둠
    if i in m : # 리스트의 원소 i가 입력받은 m에 있다면
       m = m.replace(i[0:3], i[0]) # 알파벳을 하나로 줄여줌
                                    # apa -> a, epe -> e ...
print(m)


    