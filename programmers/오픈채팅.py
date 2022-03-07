def solution(record):
    
    answer = []
    users = {}

    for str in record:
        strlist = str.split()
        action = strlist[0]
        if action == 'Enter' or action == 'Change':
            id = strlist[1]
            name = strlist[2]
            users[id] = name
    
    for str in record:
        strlist = str.split()
        cmd = strlist[0]
        if cmd == 'Enter':
            id == strlist[1]
            answer.append(users[id]+ '님이 들어왔습니다.')
        elif cmd == 'Leave':
            id = strlist[1]
            answer.append(users[id] + '님이 나갔습니다.')

    return answer