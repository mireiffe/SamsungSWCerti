import sys
sys.stdin = open("input.txt", 'r')


class Solve(object):
    _dir = {'l': 0, 'r': 1, 'u': 2, 'd': 3}
    def __init__(self):
        self.N = int(input())
        self.A = [list(map(int, input().split())) for _ in range(self.N)]

        self.mind = self.N**2
        self.visited = [[0] * self.N for _ in range(self.N)]
        self.visited[0][0] = 1

        # self.debug = [[0] * self.N for _ in range(self.N)]

        self.dp = [[[self.N * self.N] * 4 for _ in range(self.N)] for _ in range(self.N)]


    def find_next(self, pre, r, c):
        type = self.A[r][c]
        if pre == 'l':
            if 0 < type <= 2:
                return ['l', r, c + 1],
            elif 2 < type <= 6:
                return ['d', r - 1, c], ['u', r + 1, c]
        if pre == 'r':
            if 0 < type <= 2:
                return ['r', r, c - 1],
            elif 2 < type <= 6:
                return ['d', r - 1, c], ['u', r + 1, c]
        if pre == 'u':
            if 0 < type <= 2:
                return ['u', r + 1, c],
            elif 2 < type <= 6:
                return ['r', r, c - 1], ['l', r, c + 1]
        if pre == 'd':
            if 0 < type <= 2:
                return ['d', r - 1, c],
            elif 2 < type <= 6:
                return ['r', r, c - 1], ['l', r, c + 1]
        return []

    def if_ob(self, r, c):
        up = r > self.N - 1 or c > self.N - 1
        lo = r < 0 or c < 0
        return up or lo

    def find_dist(self, r, c):
        dist = (self.N - 1 - r) + (self.N - 1 - c)
        return dist

    def dfs(self, pre, r, c, d):
        if self.mind - d <= self.find_dist(r, c):
            return

        news = self.find_next(pre, r, c)
        for np, nr, nc in news:
            if nr == self.N - 1 and nc == self.N:
                if self.mind > d:
                    self.mind = d
                    continue
            if self.if_ob(nr, nc):
                continue
            if self.A[nr][nc] == 0:
                continue
            if self.visited[nr][nc]:
                continue
            if self.dp[nr][nc][self._dir[np]] > d:
                self.dp[nr][nc][self._dir[np]] = d
                # self.debug[nr][nc] = d
                self.visited[nr][nc] = 1
                self.dfs(np, nr, nc, d+1)
                self.visited[nr][nc] = 0
                # self.debug[nr][nc] = 0

def main():
    T = int(input())
    for t in range(1, T + 1):
        slv = Solve()
        # if t < 5: continue
        # res = slv.bfs('l', 0, 0)
        slv.dfs('l', 0, 0, 0)
        print(f'#{t} {slv.mind + 1}')


if __name__=='__main__':
    main()