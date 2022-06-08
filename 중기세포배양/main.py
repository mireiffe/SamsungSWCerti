import sys
sys.stdin = open("sample_input.txt", "r")

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

class Solve(object):
    def __init__(self):
        self.R, self.C, self.K = map(int, input().split())
        S0 = [list(map(int, input().split())) for _ in range(self.R)]

        H = self.R + self.K + 2
        W = self.C + self.K + 2
        self.S = [[0] * W for _ in range(H)]

        self.ip = self.K // 2 + 1

        self.ntg = []
        for r in range(self.ip, self.ip + self.R):
            for c in range(self.ip, self.ip + self.C):
                val = S0[r - self.ip][c - self.ip]
                if val > 0:
                    self.S[r][c] = val*0x0111
                    self.ntg.append([r, c])

        for k in range(self.K):
           self.spread(k + 1)

    def spread(self, s):
        rmvs = []
        l = len(self.ntg)
        for ll in range(l):
            r, c = self.ntg[ll]
            _cv = self.S[r][c]
            cv = list(map(lambda x: int(x, 16), list(f'{_cv:04x}')))

            if cv[-1] > 0:
                self.S[r][c] -= 1
            else:
                if cv[-2] == cv[-3] :
                    for dr in range(4):
                        _r =  r + dy[dr]
                        _c =  c + dx[dr]
                        if self.S[_r][_c] == 0:
                            self.ntg.append([_r, _c])
                            self.S[_r][_c] = cv[-3] * 0x111 + s * 0x1000
                        elif self.S[_r][_c] // 0x1000 == s and ((self.S[_r][_c] % 0x1000) // 0x111 < cv[-3]):
                            self.ntg.append([_r, _c])
                            self.S[_r][_c] = cv[-3] * 0x111 + s * 0x1000
                if cv[-2] == 1:
                    rmvs.append([r, c])
                    continue
                self.S[r][c] -= 16
        for rmv in rmvs:
            self.S[rmv[0]][rmv[1]] = -1
            self.ntg.remove(rmv)

def main():
    T = int(input())
    for t in range(1, T + 1):
        slv = Solve()
        # if t > 2: continue

        print(f'#{t} {len(slv.ntg)}')

if __name__ == '__main__':
    main()

