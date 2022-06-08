import sys
sys.stdin = open("sample_input.txt", "r")


class Solve(object):
    def __init__(self):
        self.D, self.W, self.K = map(int, input().split())
        self.F = [list(map(int, input().split())) for _ in range(self.D)]

        self.As = (0,) * self.K
        self.Bs = (1,) * self.K

        self.remem = [0] * self.D
        self.res = self.D

    def checkif(self):
        isok = 0

        for c in range(self.W):
            cnt = 1
            for r in range(self.D - 1):
                if self.F[r][c] == self.F[r + 1][c]:
                    cnt += 1
                else:
                    cnt = 1
                if cnt == self.K:
                    isok += 1
                    break
            if isok < c + 1:
                break

        if isok == self.W:
            return True
        else:
            return False


    def dfs(self, layer, tp, depth):
        self.remem[layer] = 1
        mem = self.F[layer][:]
        self.F[layer] = [tp] * self.W

        if self.checkif():
            self.res = min(self.res, depth)
        else:
            for l in range(layer+1, self.D):
                if self.remem[l] == 0:
                    self.dfs(l, 0, depth + 1)
                    self.dfs(l, 1, depth + 1)

        self.F[layer] = mem
        self.remem[layer] = 0




def main():
    T = int(input())
    for t in range(1, T + 1):
        slv = Solve()
        # if t != 3: continue
        if slv.checkif():
            print(f'#{t} {0}')
        else:
            for l in range(slv.D):
                slv.dfs(l, 0, 1)
                slv.dfs(l, 1, 1)
            print(f'#{t} {slv.res}')


if __name__=='__main__':
    main()
