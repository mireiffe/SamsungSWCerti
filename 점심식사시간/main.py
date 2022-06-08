import sys
sys.stdin = open("sample_input.txt", "r")


class Solve(object):
    def __init__(self):
        self.N = int(input())
        self.map = [list(map(int, input().split())) for _ in range(self.N)]

        self.strs = []
        for r in range(self.N):
            for c in range(self.N):
                if self.map[r][c] > 1:
                    self.strs.append((r, c, self.map[r][c]))

        self.ps = []
        for r in range(self.N):
            for c in range(self.N):
                if self.map[r][c] == 1:
                    self.ps.append([abs(r - stair[0]) + abs(c - stair[1]) for stair in self.strs])

    def simulation(self, case):
        if case == 0b111000:
            dbg = 1
        s = 0
        infield = list(range(len(self.ps)))
        waiting = [[], []]
        instair = [[], []]
        gone = []
        while 1:
            s += 1

            _str = []
            for k, istr0 in enumerate(instair[0]):
                istr0[-1] += 1
                if istr0[-1] >= self.strs[0][-1]:
                    gone.append(istr0[0])
                    _str.append(istr0)
            for _s in _str:
                instair[0].remove(_s)

            _str = []
            for k, istr1 in enumerate(instair[1]):
                istr1[-1] += 1
                if istr1[-1] >= self.strs[1][-1]:
                    gone.append(istr1[0])
                    _str.append(istr1)
            for _s in _str:
                instair[1].remove(_s)

            _ifd = []
            for ifd in infield:
                dist_case = self.ps[ifd][case & (1 << ifd) > 0]
                if dist_case < s:
                    waiting[case & (1 << ifd) > 0].append(ifd)
                    _ifd.append(ifd)
            for _i in _ifd:
                infield.remove(_i)

            while waiting[0] and len(instair[0]) < 3:
                instair[0].append([waiting[0].pop(0), 0])
            while waiting[1] and len(instair[1]) < 3:
                instair[1].append([waiting[1].pop(0), 0])

            if len(gone) == len(self.ps):
                break
        return s

    def allcases(self):
        res = 1E+10
        for case in range(1 << len(self.ps)):
            res = min(self.simulation(case), res)
        return res

def main():
    T = int(input())
    for t in range(1, T + 1):
        slv = Solve()
        # if t != 1: continue
        res = slv.allcases()
        print(f'#{t} {res}')

if __name__=='__main__':
    main()