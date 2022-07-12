# 상하좌우
# 정사각형의 크기의 배열을 움진다.
# L : Left, R : Right, U : Up, D : Down

N = int(input())

x, y = 0, 0

positions = input().split()

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

move_types = ['U','D', 'L', 'R']

for plan in positions:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 0 or ny < 0 or nx > N or ny > N:
        continue
    x, y = nx, ny
print(x, y)