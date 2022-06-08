import sys
sys.stdin = open("sample_input.txt", "r")

dr = (0, -1, 1, 0, 0)
dc = (0, 0, 0, -1 ,1)


class Solve(object):
    def __init__(self):
        self.N, self.M, self.K = map(int, input().split())
        ipts = [list(map(int, input().split())) for _ in range(self.K)]

        self.cell = [ipt[:2] for ipt in ipts]
        self.info = [ipt[2:] for ipt in ipts]

    def simul(self):
        for m in range(1, self.M + 1):
            stack = {}
            for k in range(self.K):
                if self.info[k][0] == 0: continue
                rc = self.cell[k]
                info = self.info[k]
                rc[0] = rc[0] + dr[info[-1]]
                rc[1] = rc[1] + dc[info[-1]]
                if not (1 <= rc[0] < self.N - 1 and 1 <= rc[1] < self.N - 1):
                    info = self.info[k]
                    info[0] = info[0] // 2
                    info[1] = info[1] + (-1)**(info[1] + 1)
                if (rc[0], rc[1]) in stack.keys():
                    stack[(rc[0], rc[1])].append(k)
                else:
                    stack[(rc[0], rc[1])] = [k]

            for idx in stack.values():
                if len(idx) > 1:
                    pops = [self.info[_k][0] for _k in idx]
                    mpop = max(pops)
                    spop = sum(pops)
                    for ck in idx:
                        if self.info[ck][0] == mpop:
                            self.info[ck][0] = spop
                        else:
                            self.info[ck][0] = 0

        res = sum(list(zip(*self.info))[0])
        return res

def main():
    T = int(input())
    for t in range(1, T + 1):
        slv = Solve()

        res = slv.simul()
        print(f'#{t} {res}')

if __name__=='__main__':
    main()