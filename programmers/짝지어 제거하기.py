def solution(s):
    stack = []

    for i in range(len(s)):
        if not stack: # 스택에 비어 있을때 
            stack.append(s[i]) # 스택에 s[i]번째 단어를 넣는다
        else: #스택에 비어 있지 않을때
            if stack[-1] == s[i]: #스택에 들어가있는 단어와 s[i]번째 단어가 같은지 비교한다.
                stack.pop() #같다면 밖으로 꺼낸다
            else: #다르다면 
                stack.append(s[i]) # 스택에 넣는다.
    if stack == 0 : return 1
    else : return 0