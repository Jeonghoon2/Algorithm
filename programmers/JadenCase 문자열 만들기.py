# JadenCase 문자열 만들기

def solution(s):
    answer = ''

    # 문자열 쪼개기
    s = s.split(' ')

    for i in range(len(s)):

        # 첫번째 문짜 대문자로 바꾸기
        s[i] = s[i].capitalize()
    answer=' '.join(s)
    return answer

#print(solution('3people unFollowed me'))