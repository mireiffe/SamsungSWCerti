# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''
import sys

'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
sys.stdin = open("input.txt", "r")

T = int(input())

import itertools
def findSquare(v, C):
    ml = len(v)
    res = 0
    for l in range(ml, 0, -1):
        for p in itertools.permutations(v, l):
            if sum(p) > C:
                continue
            else:
                _res = sum([_p**2 for  _p in p])
                if _res > res:
                    res = _res
    return res

def argMax(A, m ,n):
    ids = [[r, c] for r in range(m) for c in range(n)]
    fA = [A[i][j] for i in range(m) for j in range(n)]

    resfA = sorted(range(len(fA)), key=lambda x: fA[x])
    return [ids[rf] for rf in resfA[::-1]], sorted(fA)[::-1]

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
res = []
for t in range(1, T + 1):
    N, M, C = list(map(int, input().split(' ')))
    A = [list(map(int, input().split(' '))) for _ in range(N)]

    B = []
    SB = []
    for a in A:
        B.append([])
        SB.append([])
        for i in range(N - M + 1):
            _a = sorted(a[i:i + M])[::-1]
            SB[-1].append(findSquare(_a, C))
    ids, sb = argMax(SB, N, N - M + 1)

    for i in range(1, C+1):
        if ids[i][0] != ids[0][0]:
            res.append(f'#{t} {sb[0] + sb[i]}')
            break
        elif abs(ids[i][1] - ids[0][1]) >= C:
            res.append(f'#{t} {sb[0] + sb[i]}')
            break

print(*res, sep='\n')




