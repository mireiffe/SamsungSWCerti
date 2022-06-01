# import sys
# sys.stdin = open("input.txt", "r")

def solve(px, py, x, y, cnt):
    global ans, ex, ey
    if x == ex and y == ey:
        ans = min(ans, cnt)
        return

    if not (0 <= x < N and 0 <= y < N):
        return

    if visited[y][x] == 1:
        return
    visited[y][x] = 1

    if px == x and py == y - 1:
        if cnt < depth[y][x][0]:
            depth[y][x][0] = cnt
            if 0 < data[y][x] <= 2:
                solve(x, y, x, y + 1, cnt + 1)
            elif data[y][x] > 2:
                solve(x, y, x - 1, y, cnt + 1)
                solve(x, y, x + 1, y, cnt + 1)

    elif px == x and py == y + 1:
        if cnt < depth[y][x][1]:
            depth[y][x][1] = cnt
            if 0 < data[y][x] <= 2:
                solve(x, y, x, y - 1, cnt + 1)
            elif data[y][x] > 2:
                solve(x, y, x + 1, y, cnt + 1)
                solve(x, y, x - 1, y, cnt + 1)

    elif px == x - 1 and py == y:
        if cnt < depth[y][x][2]:
            depth[y][x][2] = cnt
            if 0 < data[y][x] <= 2:
                solve(x, y, x + 1, y, cnt + 1)
            elif data[y][x] > 2:
                solve(x, y, x, y + 1, cnt + 1)
                solve(x, y, x, y - 1, cnt + 1)

    else:
        if cnt < depth[y][x][3]:
            depth[y][x][3] = cnt
            if 0 < data[y][x] <= 2:
                solve(x, y, x - 1, y, cnt + 1)
            elif data[y][x] > 2:
                solve(x, y, x, y + 1, cnt + 1)
                solve(x, y, x, y - 1, cnt + 1)
    visited[y][x] = 0


T = int(input())
for test_case in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    ans = float('inf')

    for i in range(2):
        depth = [[[N * N] * 4 for _ in range(N)] for _ in range(N)]
        visited = [[0] * N for _ in range(N)]
        if not i:
            ex, ey = N, N - 1
            solve(- 1, 0, 0, 0, 0)
        else:
            ex, ey = - 1, 0
            solve(N, N - 1, N - 1, N - 1, 0)
    print(f"#{test_case + 1} {ans}")