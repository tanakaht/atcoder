import math
N = int(input())
keta = math.floor(math.log(N, 10)) + 1
ans = 0
for i in range(1, keta):
    if i % 2 == 1:
        ans += 9 * pow(10, i - 1)
if keta % 2 == 1:
    ans += N - pow(10, keta - 1)+1
print(ans)
