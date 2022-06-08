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

    def gts(self):
        for r0 in range(self.N):
            for c0 in range(self.N):
                if self.M[r0][c0] != 0: continue
                self.M[r0][c0] -= 11
                for d0 in range(4):
                    d, r, c = d0, r0, c0
                    cnt = 0
                    if r == 3 and c == 5 and d == 3:
                        dbg = 1
                    while 1:
                        r = r + dy[d]
                        c = c + dx[d]

                        if not (0 <= r < self.N and 0 <= c < self.N):
                            self.max_score = max(self.max_score, 2 * cnt + 1)
                            res = 2 * cnt + 1, 'b'
                            break
                        if self.M[r][c] < 0:
                            self.max_score = max(self.max_score, cnt)
                            res = cnt, 'x'
                            break
                        if self.R[d][r][c] != -1:
                            rcnt, tp = self.R[d][r][c]
                            if tp == 'x':
                                self.max_score = max(self.max_score, cnt + rcnt)
                                res = cnt + rcnt, 'x'
                                break
                            elif tp == 'b':
                                self.max_score = max(self.max_score, 2 * cnt + rcnt)
                                res = 2 * cnt + rcnt, 'b'
                                break

                        if 1 <= self.M[r][c] <= 5:
                            d = self.prefix[self.M[r][c]][d]
                            if d == -1:
                                self.max_score = max(self.max_score, 2 * cnt + 1)
                                res = 2 * cnt + 1, 'b'
                                break
                            cnt += 1
                        if 6 <= self.M[r][c] <= 10:
                            if self.prefix[self.M[r][c]][0] == (r, c):
                                r, c = self.prefix[self.M[r][c]][1]
                            else:
                                r, c = self.prefix[self.M[r][c]][0]
                    self.R[d0][r0][c0] = res
                self.M[r0][c0] += 11

def main():
    T = int(input())
    for t in range(1, T + 1):
        slv = Solve()
        # if t != 6: continue
        slv.gts()

        print(f'#{t} {slv.max_score}')

if __name__ == '__main__':
    main()