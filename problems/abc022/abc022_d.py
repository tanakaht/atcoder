import math

N = int(input())
Axy = [list(map(int, input().split())) for _ in range(N)]
Bxy = [list(map(int, input().split())) for _ in range(N)]
A_base, B_base = [0, 0], [0, 0]
for x, y in Axy:
    A_base[0] += x
    A_base[1] += y
for x, y in Bxy:
    B_base[0] += x
    B_base[1] += y
A_base_x, A_base_y = [A_base[0]/N, A_base[1]/N]
B_base_x, B_base_y = [B_base[0]/N, B_base[1]/N]
a_dist = 0
b_dist = 0
for x, y in Axy:
    dist = math.sqrt((x-A_base_x)**2+(y-A_base_y)**2)
    a_dist = max(a_dist, dist)
for x, y in Bxy:
    dist = math.sqrt((x-B_base_x)**2+(y-B_base_y)**2)
    b_dist = max(b_dist, dist)
print(b_dist/a_dist)
