# 방문 길이
# 좌, 우 = x
# 상, 하 = y

# 기존 풀이
def solution(dirs):
    visit = []
    x , y = 0, 0
    for i in dirs:

        if i == 'U' :
            if not y+1 == 6:
                y += 1
                visit.append((x,y,x,y-1))

        elif i == 'D' :
            if not y-1 == -6:
                y -= 1
                visit.append((x,y,x,y+1))

        elif i == 'R':
            if not x+1 == 6:
                x += 1
                visit.append((x,y,x-1,y))

        elif i == 'L' :
            if not x-1 == -6:
                x -= 1
                visit.append((x,y,x+1,y))

    answer = len(set(visit))
    return answer

# 다른 사람 코드
def solution(dirs):
    s = set()
    d = {'U': (0,1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    x, y = 0, 0
    for i in dirs:
        nx, ny = x + d[i][0], y + d[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            s.add((x,y,nx,ny))
            s.add((nx,ny,x,y))
            x, y = nx, ny
    return len(s)//2

print(solution('LULLLLLLU'))