import sys

N = int(input())
T = input()
S = '110'*N

if T == '1':
    print(2 * 10 ** 10)
    sys.exit(0)
elif T == '0':
    print(10 ** 10)
    sys.exit(0)


for i in range(4):
    if T == S[i:N + i]:
        break
if i == 3:
    print(0)
    sys.exit(0)
ans = 10 ** 10 - (i + N-1) // 3
print(ans)
