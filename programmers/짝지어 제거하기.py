def solution(s):
    stack = []

    for i in range(len(s)):
        if stack.__sizeof__ == 0: 
            stack.append(s[i]) 
        else:  
            if stack[-1] == s[i]: 
                stack.pop() 
            else:
                stack.append(s[i])
    if stack == 0 : return 1
    else : return 0

print(solution("baabaa"))

