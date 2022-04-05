# [3차] 파일명 정렬

def solution(files):
    answer = []
    for f in files:
        head, number, tail = '', '', ''

        number_check = False
        for i in range(len(f)): # 문자열 자르기
            if f[i].isdigit():  # 처음 나오는 숫자부터는 NUMBER로
                number += f[i]
                number_check = True
            elif not number_check:  # NUMBER가 나오기 전까지는 HEAD
                head += f[i]
            else:               # NUMBER가 이미 나왔고, 숫자가 아닌 문자가 나오면 TAIL
                tail = f[i:]
                break
        # HEAD, NUMBER, TAIL 하나의 튜플로 저장
        answer.append((head, number, tail))  
    # HEAD 우선, NUMBER 차선으로 정렬
    answer.sort(key=lambda x: (x[0].upper(), int(x[1])))
    # 원래 문자형으로 변경
    return [''.join(t) for t in answer]   

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))