import sys
N = int(input())
A = list(map(int, input().split()))
sumA = sum(A)
if sumA%10!=0:
    print('No')
    sys.exit(0)

r = 0
tmp = 0
for l in range(N):
    while sumA//10>tmp:
        tmp += A[r%N]
        r += 1
    if sumA//10==tmp:
        print('Yes')
        sys.exit(0)
    tmp -= A[l]
print('No')
