import sys
sys.stdin = open("sample_input.txt", "r")


dx = [0, 0, 1, 0, -1]
dy = [0, -1, 0, 1, 0]


class Solve(object):
    def __init__(self):
        self.M, self.A = map(int, input().split())
        self.ma = list(map(int, input().split()))
        self.mb = list(map(int, input().split()))
        self.ma.append(0)
        self.mb.append(0)
        self.E = 0

        self.info = [list(map(int, input().split())) for _ in range(self.A)]
        for ii in self.info:
            ii[0] -= 1
            ii[1] -= 1
        self.info.sort(key=lambda x: x[3], reverse=False)

        self.map = [[0]*10 for _ in range(10)]
        for r in range(10):
            for c in range(10):
                for k, ii in enumerate(self.info):
                    l1norm = abs(ii[0] - c) + abs(ii[1] - r)
                    if l1norm <= ii[2]:
                        self.map[r][c] = self.map[r][c] | (1 << k)

    def find_max(self, info):
        for i in range(self.A):
            if info >> i == 1:
                break
        return i

    def movement(self):
        ax, ay = 0, 0
        bx, by = 9, 9
        for s in range(self.M + 1):
            na = self.map[ay][ax]
            nb = self.map[by][bx]
            if s == 30:
                dbg = 1

            if na == 0 and nb == 0:
                ax, ay = ax + dx[self.ma[s]], ay + dy[self.ma[s]]
                bx, by = bx + dx[self.mb[s]], by + dy[self.mb[s]]
                continue
            if na == 0 and nb != 0:
                ax, ay = ax + dx[self.ma[s]], ay + dy[self.ma[s]]
                bx, by = bx + dx[self.mb[s]], by + dy[self.mb[s]]
                self.E += self.info[self.find_max(nb)][-1]
                continue
            if na != 0 and nb == 0:
                ax, ay = ax + dx[self.ma[s]], ay + dy[self.ma[s]]
                bx, by = bx + dx[self.mb[s]], by + dy[self.mb[s]]
                self.E += self.info[self.find_max(na)][-1]
                continue

            # now na != 0 and nb != 0
            Ma = self.find_max(na)
            Mb = self.find_max(nb)
            if Ma != Mb:
                self.E += self.info[Ma][-1] + self.info[Mb][-1]
                ax, ay = ax + dx[self.ma[s]], ay + dy[self.ma[s]]
                bx, by = bx + dx[self.mb[s]], by + dy[self.mb[s]]
                continue
            if Ma == Mb:
                na2 = na - (1 << Ma)
                nb2 = nb - (1 << Mb)
                if na2 == 0 and nb2 == 0:
                    self.E += self.info[Ma][-1]
                    ax, ay = ax + dx[self.ma[s]], ay + dy[self.ma[s]]
                    bx, by = bx + dx[self.mb[s]], by + dy[self.mb[s]]
                    continue
                if na2 == 0 and nb2 != 0:
                    Mab2 = self.find_max(nb2)
                    ax, ay = ax + dx[self.ma[s]], ay + dy[self.ma[s]]
                    bx, by = bx + dx[self.mb[s]], by + dy[self.mb[s]]
                    # if self.info[Ma][-1] / 2 > self.info[Mab2][-1]:
                    #     self.E += self.info[Ma][-1]
                    # else:
                    self.E += self.info[Ma][-1] + self.info[Mab2][-1]
                    continue
                if na2 != 0 and nb2 == 0:
                    Mab2 = self.find_max(na2)
                    ax, ay = ax + dx[self.ma[s]], ay + dy[self.ma[s]]
                    bx, by = bx + dx[self.mb[s]], by + dy[self.mb[s]]
                    # if self.info[Ma][-1] / 2 > self.info[Mab2][-1]:
                    #     self.E += self.info[Ma][-1]
                    # else:
                    self.E += self.info[Ma][-1] + self.info[Mab2][-1]
                    continue
                if na2 != 0 and nb2 != 0:
                    Mab2 = max(self.find_max(na2), self.find_max(nb2))
                    ax, ay = ax + dx[self.ma[s]], ay + dy[self.ma[s]]
                    bx, by = bx + dx[self.mb[s]], by + dy[self.mb[s]]
                    # if self.info[Ma][-1] / 2 > self.info[Mab2][-1]:
                    #     self.E += self.info[Ma][-1]
                    # else:
                    self.E += self.info[Ma][-1] + self.info[Mab2][-1]
                    continue

def main():
    T = int(input())
    for t in range(1, T + 1):
        slv = Solve()
        # if t != 4: continue
        slv.movement()

        print(f'#{t} {slv.E}')

if __name__ == '__main__':
    main()