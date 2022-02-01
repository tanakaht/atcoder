import math

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
C = [x+1j*y for x, y in XY]
ans = math.inf
for i in range(N):
    x0, y0 = XY[i]
    Cs = []
    for j in range(N):
        if i==j:
            continue
        x, y = XY[j]
        Cs.append(math.atan2(y-y0, x-x0))
    Cs = sorted(Cs)+[math.pi*2+c for c in sorted(Cs)]
    j = 0
    for c in Cs[:N-1]:
        while Cs[j+1]<c+math.pi:
            j += 1
        ans = min(ans, abs(Cs[j]-(c+math.pi)), abs(Cs[j+1]-(c+math.pi)))
print(180*(math.pi-ans)/math.pi)
