# 에디터
# 1406번

from asyncio.windows_events import NULL


txt = list(input())
cursor = len(txt)

for i in range(int(input())):
    co = list(input().split())

    if co[0] == 'P':
        txt.insert(cursor, co[1])
    elif co[0] == 'L':
        if cursor > 0:
            cursor -=1
    elif co[0] =='D':
        if cursor <len(txt):
            cursor += 1
    else:
        if cursor > 0:
            txt.remove(txt[cursor-1])