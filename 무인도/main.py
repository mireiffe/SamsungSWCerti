import sys
sys.stdin = open("input.txt", 'r')


# 2 <= N <= 20
# 1 <= boxes <= 1000


class Solve(object):
    # H x Area
    chs = [(0, 1, 2), (1, 2, 0), (2, 0, 1)]
    def __init__(self):
        self.N = int(input())
        self.B = [list(map(int, input().split())) for _ in range(self.N)]
        self.used = [0]*self.N
        self.maxsides = [max(box) for box in self.boxes]

        self.boxes = [[(b[ch[0]], b[ch[1]], b[ch[2]]) for ch in self.chs] for b in self.B]
        self.memo = [[[0]*(1<<self.N) for _ in range(sum(self.maxsides))] for _ in range(self.N)]

        self.H = 0
        self.maxH = 0

    @staticmethod
    def check_if(btm, top):
        c1 = btm[0] >= top[0] and btm[1] >= top[1]
        c2 = btm[0] >= top[1] and btm[1] >= top[0]
        if c1 or c2:
            return True
        else:
            return False

    @staticmethod
    def addbox(lst_box, i):
        return lst_box + (1 << i)

    @staticmethod
    def rmvbox(lst_box, i):
        return lst_box - (1 << i)

    def dfs(self, b0, b, d, lst_box):
        if self.maxH < self.H:
            self.maxH = self.H
        if d == self.N:
            return
        # if self.memo[d][self.H][lst_box]:
        #     self.maxH = self.memo[d][self.H][lst_box]
        #     return

        remain = sum([self.maxsides[i] for i, u in enumerate(self.used) if u == 0])
        if self.maxH >= remain + self.H:
            return

        for k, box in enumerate(self.boxes):
            if self.used[k]:
                continue
            self.used[k] = 1
            for ch in self.chs:
                nb = [box[ch[1]], box[ch[2]]]
                if not self.check_if(b, nb):
                    continue
                self.H += box[ch[0]]
                lst_box = self.addbox(lst_box, k)
                self.dfs(b, nb, d + 1, lst_box)
                lst_box = self.rmvbox(lst_box, k)
                self.H -= box[ch[0]]
            self.used[k] = 0
        # self.memo[d][self.H][lst_box] = self.maxH

def main():
    T = int(input())
    for t in range(1, T + 1):
        slv = Solve()
        slv.dfs([10000, 10000], [10000, 10000], 0, 0)
        print(f'#{t} {slv.maxH}')


if __name__=='__main__':
    main()