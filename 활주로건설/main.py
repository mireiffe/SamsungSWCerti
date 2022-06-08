import sys
sys.stdin = open("sample_input.txt", "r")


class Solve(object):
    def __init__(self):
        self.N, self.X = map(int, input().split())
        self.H = [list(map(int, input().split())) for _ in range(self.N)]
        self.HT = [list(ht) for ht in zip(*self.H)]

        self.res = 0

    def walking(self, H):
        for hs in H:
            cnt = 1
            if max(hs) == min(hs):
                self.res += 1
                continue
            downflg = 0
            duflg = 0
            ph = hs[0]
            for k, h in enumerate(hs[1:]):
                diff = ph - h
                ph = h
                if abs(diff) > 1:
                    break
                elif diff == 0:
                    cnt += 1
                    if downflg and (cnt >= self.X):
                        downflg = 0
                        duflg = 1
                        cnt = 0
                    elif duflg:
                        duflg = 0
                elif diff == -1:
                    if downflg:
                        break
                    elif cnt < self.X:
                        break
                    elif duflg:
                        break
                    else:
                        cnt = 1
                elif diff == 1:
                    if downflg:
                        break
                    elif duflg:
                        duflg = 0
                    downflg = 1
                    cnt = 1
                if k == self.N - 2 and not downflg:
                    self.res += 1

def main():
    T = int(input())
    for t in range(1, T + 1):
        slv = Solve()
        # if t != 6: continue
        slv.walking(slv.H)
        slv.walking(slv.HT)
        print(f'#{t} {slv.res}')

if __name__ == '__main__':
    main()