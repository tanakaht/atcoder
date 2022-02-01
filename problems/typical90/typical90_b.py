import sys
N = int(input())
if N%2==1:
    print()
    sys.exit(0)

def is_ok(bit):
    n = 0
    for i in range(N-1, -1, -1):
        if (bit>>i)&1:
            n -= 1
        else:
            n += 1
        if n < 0:
            return False
    return n==0

s = '()'
for bit in range(1<<N):
    if is_ok(bit):
        print(''.join([s[(bit>>i)&1] for i in range(N-1, -1, -1)]))
