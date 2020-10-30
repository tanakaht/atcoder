import sys

N = int(input())
apow = 1
for a in range(1, N+1):
    apow *= 3
    if apow > N:
        print(-1)
        sys.exit()
    bpow = 1
    for b in range(1, N+1):
        bpow *= 5
        if N == bpow + apow:
            print(a, b)
            sys.exit(0)
        if N < bpow + apow:
            break
