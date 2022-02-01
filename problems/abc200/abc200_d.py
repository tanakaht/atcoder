# bit全探索ver
import sys
N = int(input())
A = list(map(int, input().split()))
avilable = [False]*200
for bit in range(1, 202):
    if bit.bit_length() > N:
        break
    rest = 0
    for i in range(N):
        if (bit>>i)&1:
            rest = (rest+A[i])%200
    if avilable[rest]:
        print('Yes')
        ans1, ans2 = [], []
        for i in range(N):
            if (avilable[rest]>>i)&1:
                ans1.append(i+1)
            if (bit>>i)&1:
                ans2.append(i+1)
        print(len(ans1), *ans1)
        print(len(ans2), *ans2)
        sys.exit(0)
    avilable[rest] = bit
print('No')
