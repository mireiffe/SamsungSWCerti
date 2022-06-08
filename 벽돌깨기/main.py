import sys
sys.stdin = open("sample_input.txt", "r")

import copy


class Solve(object):
    def __init__(self):
        self.N, self.W, self.H = map(int, input().split())
        self.M = [[list(map(int, input().split())) for _ in range(self.H)][::-1]]
        self.M[0] = list(map(list, zip(*self.M[0])))
        for i in range(self.N):
            self.M.append([[0]*self.H for _ in range(self.W)])
        self.cnt = self.H * self.W

    def drop(self, d):
        if sum(sum(self.M[d], [])) == 0:
            self.cnt = 0
            return
        if d + 1 > self.N:
            self.cnt = min(sum(map(bool, sum(self.M[d], []))), self.cnt)
            return

        for w in range(self.W):
            if d == 0 and w == 2:
                dbg = 1
            if d == 1 and w == 2:
                dbg = 1
            for h in range(self.H):
                if self.M[d][w][-1-h] > 0:
                    break
                if d == 1 and w == 2 and h == 2:
                    dbg = 1

            self.M[d+1] = copy.deepcopy(self.M[d])
            ntg = [(h, w)]
            while ntg:
                h, w = ntg.pop(0)
                cn = self.M[d+1][w][-1-h]
                if cn <= 0:
                    continue
                self.M[d+1][w][-1-h] = -1
                dist = cn - 1
                if dist == 0:
                    continue
                for dst in range(dist):
                    if h - dst - 1 >= 0: ntg.append((h - dst - 1, w))
                    if h + dst + 1 < self.H: ntg.append((h + dst + 1, w))
                    if w - dst - 1 >= 0: ntg.append((h, w - dst - 1))
                    if w + dst + 1 < self.W: ntg.append((h, w + dst + 1))
            self.gravity(d)
            self.drop(d + 1)

    def gravity(self, d):
        for w in range(self.W):
            nmo = self.M[d+1][w].count(-1)
            for i in range(nmo):
                self.M[d+1][w].remove(-1)
            self.M[d+1][w] += [0] * nmo

def main():
    T = int(input())
    for t in range(1, T+1):
        slv = Solve()
        # if t > 1: continue
        slv.drop(0)

        print(f'#{t} {slv.cnt}')

if __name__ == '__main__':
    main()