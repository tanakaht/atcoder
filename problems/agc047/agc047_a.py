import sys
import decimal
import numpy as np
input = sys.stdin.readline

N = int(input())
A = []
C2 = np.array([[0 for j in range(30)] for i in range(14)])  # 10countは9タス
C5 = np.array([[0 for j in range(30)] for i in range(14)])
C10 = np.zeros(14)
for _ in range(N):
    i = decimal.Decimal(input())
    c10, c2, c5 = 0, 0, 0
    while i % 1 != 0:
        c10 -= 1
        i *= 10
    while i % 10 == 0:
        c10 += 1
        i /= 10
    while i % 2 == 0:
        c2 += 1
        i /= 2
    while i % 5 == 0:
        c5 += 1
        i /= 5
    c2 = min(c2, 30)
    c5 = min(c5, 30)
    A.append((c10, c2, c5))
    C2[c10+9][c2] += 1
    C5[c10+9][c5] += 1
    C10[c10+9] += 1

ans = 0
for i in range(14):
    ans += C10[i]*np.sum(C10[18-i:])
    if i >= 9:
        ans -= C10[i]
    for j in range(18-i):
        if j >= 14:
            continue
        for k in range(1, 30):
            shouldhave = 18 - i - j
            if k >= shouldhave:
                ans += C2[i][k] * np.sum(C5[j][shouldhave:])
                ans += C5[i][k] * np.sum(C2[j][shouldhave:])

print(int(ans//2))
