import sys
sys.stdin = open("input.txt", "r")

import math

# 조건: left >= right

class solve():
    lrset = {'l': 0, 'r':1}
    def __init__(self):
        self.N = int(input())
        self.W = list(map(int, input().split()))

        self.S = sum(self.W) / 2
        self.used = [0] * self.N
        self.cnt = 0

        self.lst = [[[-1]*(1<<self.N) for _ in range(1<<self.N)] for _ in range(self.N)]

    def addW(self, lst, i):
        return lst + (1 << i)

    def rmvW(self, lst, i):
        return lst - (1 << i)

    def dfs(self, l, r, d, lst_l, lst_r):
        if l < r:
            return
        if d == self.N:
            self.cnt += 1
            return
        if self.lst[d][lst_l][lst_r] > -1:
            self.cnt += self.lst[d][lst_l][lst_r]
            return

        if l >= self.S:
            self.cnt += (1 << (self.N - d)) * math.factorial(self.N - d)
            return
        cnt = self.cnt
        for k, nw in enumerate(self.W):
            if self.used[k]: continue
            self.used[k] = 1
            lst_l = self.addW(lst_l, k)
            self.dfs(l + nw, r, d+1, lst_l, lst_r)
            lst_l = self.rmvW(lst_l, k)

            lst_r = self.addW(lst_r, k)
            self.dfs(l, r + nw, d+1, lst_l, lst_r)
            lst_r = self.rmvW(lst_r, k)
            self.used[k] = 0
        self.lst[d][lst_l][lst_r] = self.cnt - cnt


def main():
    T = int(input())

    for t in range(1, T+1):
        slv = solve()
        slv.dfs(0, 0, 0, 0, 0)
        print(f'#{t} {slv.cnt}')


# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
if __name__ == '__main__':
    main()

