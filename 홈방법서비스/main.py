import sys
sys.stdin = open("sample_input.txt", "r")


class Solve(object):
    def __init__(self):
        self.N, self.M = map(int, input().split())
        self.C = [list(map(int, input().split())) for _ in range(self.N)]

        self.H = 0
        self.info = {}
        for r in range(self.N):
            for c in range(self.N):
                if self.C[r][c] == 1:
                    # dist < K
                    self.info[self.H] = {
                        'pos': (r, c),
                        'dist': [[abs(r - j) + abs(c - i) for i in range(self.N)] for j in range(self.N)]
                    }
                    self.H += 1
        self.res = 0

    def simul(self):
        K = 1
        while True:
            cost = K ** 2 + (K - 1) ** 2
            for r in range(self.N):
                for c in range(self.N):
                    cnt = 0
                    for nh in self.info:
                        if self.info[nh]['dist'][r][c] < K:
                            cnt += 1
                    if cnt > self.res and cost <= self.M * cnt:
                        self.res = cnt
                    if cnt == self.H:
                        return
            K += 1

def main():
    T = int(input())
    for t in range(1, T + 1):
        slv = Solve()

        slv.simul()

        print(f'#{t} {slv.res}')

if __name__=='__main__':
    main()