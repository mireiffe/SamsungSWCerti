import sys
sys.stdin = open("sample_input.txt", "r")

# directions =
# 0 1 2 3
# u r d l

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

class Solve(object):
    def __init__(self):
        self.N = int(input())
        self.M = [list(map(int, input().split())) for _ in range(self.N)]

        self.prefix = [
            None,
            [-1, -1, 1, 0],
            [1, -1, -1, 2],
            [3, 2, -1, -1],
            [-1, 0, 3, -1],
            [-1, -1, -1, -1],
            [],
            [],
            [],
            [],
            [],
        ]
        for i in range(self.N):
            for j in range(self.N):
                if self.M[i][j] > 5:
                    self.prefix[self.M[i][j]].append((i, j))

        self.R = [[[-1]*self.N for _ in range(self.N)] for __ in range(4)]
        self.max_score = 0

    def dfs(self, r, c, d):
        cnt = 0
        while 1:
            r = r + dy[d]
            c = c + dx[d]

            if not (0 <= r < self.N and 0 <= c < self.N):
                self.max_score = max(self.max_score, 2*cnt + 1)
                return 2*cnt + 1, 'b'
            if self.M[r][c] < 0:
                self.max_score = max(self.max_score, cnt)
                return cnt, 'x'

            if self.R[d][r][c] !=  -1:
                rcnt, tp = self.R[d][r][c]
                if tp == 'x':
                    self.max_score = max(self.max_score, cnt + rcnt)
                    return cnt + rcnt, 'x'
                elif tp == 'b':
                    self.max_score = max(self.max_score, 2 * cnt + rcnt)
                    return 2 * cnt + rcnt, 'b'

            if 1 <= self.M[r][c] <= 5:
                d = self.prefix[self.M[r][c]][d]
                if d == -1:
                    self.max_score = max(self.max_score, 2*cnt + 1)
                    return 2*cnt + 1, 'b'
                cnt += 1
            if 6 <= self.M[r][c] <= 10:
                if self.prefix[self.M[r][c]][0] == (r, c):
                    r, c = self.prefix[self.M[r][c]][1]
                else:
                    r, c = self.prefix[self.M[r][c]][0]

    def gts(self):
        for r in range(self.N):
            for c in range(self.N):
                if self.M[r][c] != 0: continue
                self.M[r][c] -= 11
                for i in range(4):
                    self.R[i][r][c] = self.dfs(r, c, i)
                self.M[r][c] += 11

def main():
    T = int(input())
    for t in range(1, T + 1):
        slv = Solve()
        # if t != 6: continue
        slv.gts()

        print(f'#{t} {slv.max_score}')

if __name__ == '__main__':
    main()