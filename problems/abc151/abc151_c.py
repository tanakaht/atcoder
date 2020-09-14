N, M = map(int, input().split())
flgs = [0] * N
penas = [0] * N
ac = 0
pena = 0
for _ in range(M):
    p, s = input().split()
    p = int(p)
    s = (s=='AC')
    if flgs[p - 1]:
        continue
    elif s:
        ac += 1
        flgs[p - 1] = 1
        pena += penas[p-1]
    else:
        penas[p - 1] += 1

print(ac, pena)
