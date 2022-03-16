# 암호 만들기
# 서로 다른 L개의 알파벳 소문자들로 구성
# 최소 한개의 모음 포함, 최소 두개의 자음으로 구성

# 내장 함수 Combinations를 사용 해야 한다.

from itertools import combinations
 
word_max_num, word_count = map(int,input().split())
alphabet = sorted(input().split())
sekretkey = combinations(alphabet, word_max_num)
 
for word in sekretkey:
    cnt_vow = 0
    for i in word:
        if i in "aeiou":
            cnt_vow += 1
 
    if cnt_vow >=1 and word_max_num - cnt_vow >=2:
        print(''.join(word))