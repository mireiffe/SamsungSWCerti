import sys
sys.stdin = open("sample_input.txt", "r")

num_nal = 8
num_whl = 4


class Solve(object):
    def __init__(self):
        self.K = int(input())
        self.mags = [list(map(int, input().split())) for _ in range(num_whl)]
        self.rots = [list(map(int, input().split())) for _ in range(self.K)]
        for rot in self.rots:
            rot[0] -= 1

        self.reds = [0] * num_whl

    def rotation(self, nw):
        if self.tbrot[nw]:
            return
        self.tbrot[nw] = 1

        ntg = []
        if nw - 1 >= 0 and self.tbrot[(nw - 1) % num_whl] == 0:
            mag0 = self.mags[nw][(self.reds[nw] - 2) % num_nal]
            mag1 = self.mags[nw - 1][(self.reds[nw - 1] + 2) % num_nal]
            if mag0 + mag1 == 1:
                ntg.append(nw - 1)
        if nw + 1 < num_whl and self.tbrot[(nw + 1) % num_whl] == 0:
            mag0 = self.mags[nw][(self.reds[nw] + 2) % num_nal]
            mag1 = self.mags[nw + 1][(self.reds[nw + 1] - 2) % num_nal]
            if mag0 + mag1 == 1:
                ntg.append(nw + 1)

        for n in ntg:
            self.rotation(n)

    def rotations(self):
        for rot in self.rots:
            self.tbrot = [0] * num_whl
            self.rotation(rot[0])
            for w in range(num_whl):
                if self.tbrot[w]:
                    dir_rot = int(rot[1] * (-1)**(rot[0] - w))
                    self.reds[w] = (self.reds[w] - dir_rot) % num_nal


def main():
    T = int(input())
    for t in range(1, T + 1):
        slv = Solve()

        slv.rotations()
        scores = [slv.mags[k][rds]*(1 << k) for k, rds in enumerate(slv.reds)]
        print(f'#{t} {sum(scores)}')

if __name__ == '__main__':
    main()