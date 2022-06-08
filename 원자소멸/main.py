import sys
sys.stdin = open("sample_input.txt", "r")

# drts 0 1 2 3
# drts u d l r
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


class Solve(object):
    def __init__(self):
        self.N = int(input())
        C0 = [list(map(int, input().split())) for _ in range(self.N)]

        self.bnd = [[2000, -2000], [2000, -2000]]
        self.C = []
        self.D = []
        for c0 in C0:
            self.C.append([2*c0[0], 2*c0[1]])
            self.D.append(c0[2:])
            self.bnd[0][0] = min(2*c0[0], self.bnd[0][0])
            self.bnd[0][1] = max(2*c0[0], self.bnd[0][1])
            self.bnd[1][0] = min(2*c0[1], self.bnd[1][0])
            self.bnd[1][1] = max(2*c0[1], self.bnd[1][1])

        self.E = 0

    def find_jump(self, iteridx):
        jump = 4000
        for k1 in iteridx:
            c1 = self.C[k1]
            d1 = self.D[k1][0]
            for k2 in iteridx:
                if k1 >= k2:
                    continue
                c2 = self.C[k2]
                d2 = self.D[k2][0]
                if d1 == d2:
                    continue
                elif d1 == 0 and d2 == 1:
                    if c1[0] != c2[0] or c1[1] > c2[1]:
                        continue
                    jump = min(jump, abs(c1[1] - c2[1]) // 2)
                elif d1 == 1 and d2 == 0:
                    if c1[0] != c2[0] or c1[1] < c2[1]:
                        continue
                    jump = min(jump, abs(c1[1] - c2[1]) // 2)
                elif d1 == 2 and d2 == 3:
                    if c1[1] != c2[1] or c1[0] < c2[0]:
                        continue
                    jump = min(jump, abs(c1[0] - c2[0]) // 2)
                elif d1 == 3 and d2 == 2:
                    if c1[1] != c2[1] or c1[0] > c2[0]:
                        continue
                    jump = min(jump, abs(c1[0] - c2[0]) // 2)
                else:
                    if abs(c1[0] - c2[0]) == abs(c1[1] - c2[1]):
                        jump = min(jump, abs(c1[0] - c2[0]))
                jump = max(jump, 1)
        return jump

    def moving(self):
        rmvs = []
        while 1:
            iteridx = [i for i in range(self.N) if i not in rmvs]
            if len(rmvs) >= self.N - 1:
                break
            jump = self.find_jump(iteridx)
            for k in iteridx:
                c = self.C[k]
                d = self.D[k]
                c[0] = c[0] + jump * dx[d[0]]
                c[1] = c[1] + jump * dy[d[0]]

            for k in iteridx:
                c = self.C[k]
                if not (self.bnd[0][0] <= c[0] <= self.bnd[0][1] and self.bnd[1][0] <= c[1] <= self.bnd[1][1]):
                    rmvs.append(k)
                elif self.C.count(c) > 1:
                    rmvs.append(k)
                    self.E += self.D[k][1]

            # self.bnd = [[2000, -2000], [2000, -2000]]
            # for k in iteridx:
            #     c = self.C[k]
            #     self.bnd[0][0] = min(c[0], self.bnd[0][0])
            #     self.bnd[0][1] = max(c[0], self.bnd[0][1])
            #     self.bnd[1][0] = min(c[1], self.bnd[1][0])
            #     self.bnd[1][1] = max(c[1], self.bnd[1][1])



def main():
    T = int(input())
    for t in range(1, T + 1):
        slv = Solve()
        # if t != 3: continue
        slv.moving()

        print(f'#{t} {slv.E}')

if __name__ == '__main__':
    main()