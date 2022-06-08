import sys
sys.stdin = open("sample_input.txt", "r")


class Solve(object):
    def __init__(self):
        self.N, self.K = map(int, input().split())
        self.S = input()
        self.nos = self.N // 4

        self.NS = self.S + self.S[:self.nos]

        self.nums = []

    def getAllNums(self):
        for i in range(self.N):
            if i == 9:
                tt = 1
            cn = self.NS[i:i+self.nos]
            self.nums.append(cn)

    def findKth(self):
        nums = sorted(set(self.nums))
        return nums[-self.K]

def main():
    T = int(input())
    res = []
    for t in range(1, T + 1):
        slv = Solve()
        slv.getAllNums()

        print(f'#{t} {int(slv.findKth(), 16)}')

if __name__ == '__main__':
    main()

